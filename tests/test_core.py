#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DesignPilot Test Suite - Core functionality tests
DesignPilot 核心功能测试套件
"""

import sys
import os
import json
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_presets_loading():
    """Test that all presets load correctly."""
    from src.presets import get_all_presets, get_preset, list_presets
    print("  📋 Testing presets loading...")

    presets = get_all_presets()
    assert len(presets) >= 10, f"Expected at least 10 presets, got {len(presets)}"
    print(f"    ✅ Loaded {len(presets)} presets")

    # Test individual preset
    wechat = get_preset("wechat")
    assert wechat["name"] == "WeChat"
    assert len(wechat["tokens"]["colors"]) > 0
    assert len(wechat["tokens"]["typography"]) > 0
    print(f"    ✅ WeChat preset: {len(wechat['tokens']['colors'])} colors, "
          f"{len(wechat['tokens']['typography'])} typography tokens")

    # Test fuzzy matching
    alipay = get_preset("alipay")
    assert alipay["name"] == "Alipay"
    print(f"    ✅ Alipay preset loaded")

    # Test list_presets
    preset_list = list_presets()
    assert len(preset_list) == len(presets)
    print(f"    ✅ list_presets returns {len(preset_list)} items")


def test_models():
    """Test data models."""
    from src.models import (ColorToken, TypographyToken, SpacingToken,
                            ShadowToken, BorderRadiusToken, DesignSystem)
    print("  📋 Testing data models...")

    # ColorToken
    color = ColorToken(name="primary", value="#FF0000", format="hex",
                       description="Primary color", variants={"light": "#FF6666"})
    assert color.value == "#FF0000"
    d = color.to_dict()
    assert d["name"] == "primary"
    css = color.to_css_var()
    assert "--color-primary:" in css
    print(f"    ✅ ColorToken: {css.strip()}")

    # TypographyToken
    typo = TypographyToken(name="body", family="sans-serif", size="14px",
                           weight="400", line_height="1.6")
    css = typo.to_css_var()
    assert "--font-body-family:" in css
    assert "--font-body-size:" in css
    print(f"    ✅ TypographyToken")

    # SpacingToken
    spacing = SpacingToken(name="md", value="16px")
    css = spacing.to_css_var()
    assert "--spacing-md:" in css
    print(f"    ✅ SpacingToken")

    # DesignSystem
    ds = DesignSystem(
        name="Test System",
        colors=[color],
        typography=[typo],
        spacing=[spacing],
    )
    assert ds.token_count() == 3
    json_str = ds.to_json()
    parsed = DesignSystem.from_json(json_str)
    assert parsed.name == "Test System"
    assert len(parsed.colors) == 1
    print(f"    ✅ DesignSystem serialization/deserialization")


def test_extractor():
    """Test CSS token extraction."""
    from src.extractor import DesignExtractor
    print("  📋 Testing CSS extraction...")

    css_content = """
    .button {
        background-color: #FF5000;
        color: #FFFFFF;
        padding: 12px 24px;
        margin: 8px;
        border-radius: 8px;
        font-family: 'PingFang SC', sans-serif;
        font-size: 14px;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    .container {
        padding: 16px;
        margin-bottom: 24px;
        border: 1px solid #E5E5E5;
    }
    @media (min-width: 768px) {
        .container { padding: 32px; }
    }
    """

    with tempfile.NamedTemporaryFile(mode='w', suffix='.css', delete=False) as f:
        f.write(css_content)
        temp_path = f.name

    try:
        extractor = DesignExtractor(source=temp_path, format='css')
        result = extractor.extract()

        assert len(result["colors"]) > 0, "Should extract colors"
        assert len(result["spacing"]) > 0, "Should extract spacing"
        assert len(result["typography"]) > 0, "Should extract typography"
        assert len(result["shadows"]) > 0, "Should extract shadows"
        assert len(result["borderRadius"]) > 0, "Should extract border-radius"
        assert len(result["breakpoints"]) > 0, "Should extract breakpoints"
        print(f"    ✅ Extracted: {len(result['colors'])} colors, "
              f"{len(result['spacing'])} spacing, {len(result['typography'])} typography, "
              f"{len(result['shadows'])} shadows, {len(result['borderRadius'])} radius, "
              f"{len(result['breakpoints'])} breakpoints")
    finally:
        os.unlink(temp_path)


def test_generator():
    """Test DESIGN.md generation."""
    from src.generator import DesignDocGenerator
    print("  📋 Testing DESIGN.md generation...")

    with tempfile.TemporaryDirectory() as tmpdir:
        # Test with preset
        gen = DesignDocGenerator(
            preset="wechat",
            output=os.path.join(tmpdir, "DESIGN.md"),
            lang="zh",
        )
        path = gen.generate()
        assert os.path.exists(path)

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert "# 🎨" in content
        assert "色彩体系" in content
        assert "字体排版" in content
        assert "CSS 变量" in content
        print(f"    ✅ Chinese DESIGN.md generated ({len(content)} chars)")

        # Test English version
        gen_en = DesignDocGenerator(
            preset="alipay",
            output=os.path.join(tmpdir, "DESIGN.en.md"),
            lang="en",
        )
        path_en = gen_en.generate()
        with open(path_en, 'r', encoding='utf-8') as f:
            content_en = f.read()
        assert "Color Palette" in content_en
        assert "Typography" in content_en
        print(f"    ✅ English DESIGN.md generated ({len(content_en)} chars)")


def test_preview():
    """Test HTML preview generation."""
    from src.preview import PreviewGenerator
    print("  📋 Testing HTML preview generation...")

    with tempfile.TemporaryDirectory() as tmpdir:
        gen = PreviewGenerator(
            preset="feishu",
            output=os.path.join(tmpdir, "preview.html"),
            title="Test Preview",
        )
        path = gen.generate()
        assert os.path.exists(path)

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert "<!DOCTYPE html>" in content
        assert "Feishu" in content
        assert "Color Palette" in content
        assert "Typography" in content
        print(f"    ✅ HTML preview generated ({len(content)} chars)")


def test_exporter():
    """Test multi-format export."""
    from src.exporter import DesignExporter
    print("  📋 Testing multi-format export...")

    with tempfile.TemporaryDirectory() as tmpdir:
        exporter = DesignExporter(
            preset="xiaohongshu",
            output_dir=tmpdir,
            formats=["css", "json", "tailwind", "scss", "less"],
        )
        results = exporter.export()

        assert "css" in results
        assert "json" in results
        assert "tailwind" in results
        assert "scss" in results
        assert "less" in results

        # Verify CSS content
        with open(results["css"], 'r', encoding='utf-8') as f:
            css = f.read()
        assert ":root" in css
        assert "--color-" in css
        print(f"    ✅ CSS export: {len(css)} chars")

        # Verify JSON content
        with open(results["json"], 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        assert "tokens" in json_data
        print(f"    ✅ JSON export: valid structure")

        # Verify Tailwind content
        with open(results["tailwind"], 'r', encoding='utf-8') as f:
            tw = f.read()
        assert "module.exports" in tw
        assert "theme" in tw
        print(f"    ✅ Tailwind export: {len(tw)} chars")

        # Verify SCSS content
        with open(results["scss"], 'r', encoding='utf-8') as f:
            scss = f.read()
        assert "$" in scss
        print(f"    ✅ SCSS export: {len(scss)} chars")

        # Verify LESS content
        with open(results["less"], 'r', encoding='utf-8') as f:
            less = f.read()
        assert "@" in less
        print(f"    ✅ LESS export: {len(less)} chars")


def test_validator():
    """Test design system validation."""
    from src.validator import DesignValidator
    from src.presets import get_preset
    print("  📋 Testing validation...")

    with tempfile.TemporaryDirectory() as tmpdir:
        # Save a preset as JSON
        data = get_preset("wechat")
        tokens_path = os.path.join(tmpdir, "tokens.json")
        with open(tokens_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        validator = DesignValidator(input_file=tokens_path)
        report = validator.validate()

        assert "score" in report
        assert report["score"] >= 0
        assert report["score"] <= 100
        assert "errors" in report
        assert "warnings" in report
        print(f"    ✅ Validation score: {report['score']}/100 "
              f"(E:{report['errors']} W:{report['warnings']} I:{report['infos']})")


def test_project_init():
    """Test project initialization."""
    from src.project import init_project
    print("  📋 Testing project initialization...")

    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = init_project(
            name="test-project",
            output_dir=tmpdir,
            preset="modern",
        )

        assert os.path.exists(project_path)
        assert os.path.exists(os.path.join(project_path, "DESIGN.md"))
        assert os.path.exists(os.path.join(project_path, "DESIGN.en.md"))
        assert os.path.exists(os.path.join(project_path, "preview", "index.html"))
        assert os.path.exists(os.path.join(project_path, "tokens", "design-tokens.json"))
        assert os.path.exists(os.path.join(project_path, "src", "design-tokens.css"))
        assert os.path.exists(os.path.join(project_path, ".gitignore"))
        assert os.path.exists(os.path.join(project_path, "package.json"))
        print(f"    ✅ Project initialized with all files")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("🧪 DesignPilot Test Suite")
    print("=" * 60 + "\n")

    tests = [
        ("Presets Loading", test_presets_loading),
        ("Data Models", test_models),
        ("CSS Extraction", test_extractor),
        ("DESIGN.md Generation", test_generator),
        ("HTML Preview", test_preview),
        ("Multi-format Export", test_exporter),
        ("Validation", test_validator),
        ("Project Initialization", test_project_init),
    ]

    passed = 0
    failed = 0

    for name, test_fn in tests:
        try:
            test_fn()
            passed += 1
            print(f"  ✅ {name} - PASSED\n")
        except Exception as e:
            failed += 1
            print(f"  ❌ {name} - FAILED: {e}\n")

    print("=" * 60)
    print(f"📊 Results: {passed} passed, {failed} failed, {passed + failed} total")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
