from ai_context_linker import cli


def test_demo_is_self_contained_and_does_not_scan(monkeypatch, tmp_path, capsys):
    def forbidden(*args, **kwargs):
        raise AssertionError("demo must not discover, scan, or approve real state")

    for name in ("discover_workspace", "scan_workspace", "approve_snapshot"):
        monkeypatch.setattr(cli, name, forbidden)
    output = tmp_path / "demo"
    assert cli.main(["demo", "--output-dir", str(output)]) == 0
    briefing = (output / "ai_context.md").read_text(encoding="utf-8")
    for expected in ("虚构", "食谱笔记", "周末地图", "三道菜", "周六还是周日", "README.md"):
        assert expected in briefing
    assert str(tmp_path) not in briefing
    assert "projects/recipe-notebook.md" not in briefing
    assert str((output / "ai_context.md").resolve()) in capsys.readouterr().out


def test_demo_preserves_existing_output(tmp_path):
    output = tmp_path / "demo"
    output.mkdir()
    original = output / "ai_context.md"
    original.write_text("existing real briefing", encoding="utf-8")
    assert cli.main(["demo", "--output-dir", str(output)]) == 2
    assert original.read_text(encoding="utf-8") == "existing real briefing"
    assert list(output.iterdir()) == [original]


def test_demo_is_deterministic(tmp_path):
    first, second = tmp_path / "first", tmp_path / "second"
    for output in (first, second):
        assert cli.main(["demo", "--output-dir", str(output)]) == 0
    assert {p.relative_to(first): p.read_bytes() for p in first.rglob("*") if p.is_file()} == {
        p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()
    }
