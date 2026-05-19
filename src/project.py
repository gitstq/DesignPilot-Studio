#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Initializer - Initialize new design system projects
项目初始化器

Creates a new design system project with:
- DESIGN.md from a preset
- Interactive HTML preview
- CSS custom properties file
- JSON tokens file
- .gitignore
- Project structure
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any


def init_project(name: str = "my-design-system", output_dir: str = ".",
                 preset: Optional[str] = None) -> str:
    """Initialize a new design system project."""
    project_dir = Path(output_dir) / name
    project_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Initializing design system project: {name}")
    print(f"📁 Project directory: {project_dir}")

    # Create directory structure
    dirs = ["tokens", "docs", "preview", "src"]
    for d in dirs:
        (project_dir / d).mkdir(parents=True, exist_ok=True)

    # Load preset if specified
    if preset:
        from .presets import get_preset
        data = get_preset(preset)
        print(f"🎨 Using preset: {preset}")
    else:
        from .presets import get_preset
        data = get_preset("modern")
        print(f"🎨 Using default preset: modern")

    # Save tokens JSON
    tokens_path = project_dir / "tokens" / "design-tokens.json"
    tokens_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  ✅ tokens/design-tokens.json")

    # Generate DESIGN.md (Chinese)
    from .generator import DesignDocGenerator
    gen = DesignDocGenerator(
        input_file=str(tokens_path),
        output=str(project_dir / "DESIGN.md"),
        lang="zh",
    )
    gen.generate()
    print(f"  ✅ DESIGN.md (中文版)")

    # Generate DESIGN.en.md (English)
    gen_en = DesignDocGenerator(
        input_file=str(tokens_path),
        output=str(project_dir / "DESIGN.en.md"),
        lang="en",
    )
    gen_en.generate()
    print(f"  ✅ DESIGN.en.md (English)")

    # Generate preview
    from .preview import PreviewGenerator
    preview_gen = PreviewGenerator(
        input_file=str(tokens_path),
        output=str(project_dir / "preview" / "index.html"),
        title=f"{name} Design System",
    )
    preview_gen.generate()
    print(f"  ✅ preview/index.html")

    # Export CSS
    from .exporter import DesignExporter
    exporter = DesignExporter(
        input_file=str(tokens_path),
        output_dir=str(project_dir / "src"),
        formats=["css", "tailwind", "scss"],
    )
    exporter.export()
    print(f"  ✅ src/design-tokens.css")
    print(f"  ✅ src/tailwind.config.js")
    print(f"  ✅ src/design-tokens.scss")

    # Create .gitignore
    gitignore = """# Dependencies
node_modules/
__pycache__/
*.pyc

# Build
dist/
build/
*.min.css
*.min.js

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local
"""
    (project_dir / ".gitignore").write_text(gitignore, encoding='utf-8')
    print(f"  ✅ .gitignore")

    # Create package.json for npm integration
    pkg = {
        "name": name.lower().replace(" ", "-"),
        "version": data.get("version", "1.0.0"),
        "description": data.get("description", ""),
        "main": "src/design-tokens.css",
        "files": ["src/", "tokens/"],
        "keywords": ["design-system", "design-tokens", "designpilot"],
        "license": "MIT",
    }
    (project_dir / "package.json").write_text(
        json.dumps(pkg, indent=2, ensure_ascii=False), encoding='utf-8'
    )
    print(f"  ✅ package.json")

    print(f"\n🎉 Project '{name}' initialized successfully!")
    print(f"\n💡 Next steps:")
    print(f"   cd {project_dir}")
    print(f"   # View preview: open preview/index.html")
    print(f"   # Edit tokens: tokens/design-tokens.json")
    print(f"   # Regenerate: python -m src.cli generate -i tokens/design-tokens.json")

    return str(project_dir)


def apply_preset(preset_name: str, output_dir: str = ".",
                 formats: Optional[list] = None) -> Dict[str, str]:
    """Apply a preset to current project directory."""
    from .presets import get_preset
    from .generator import DesignDocGenerator
    from .preview import PreviewGenerator
    from .exporter import DesignExporter

    data = get_preset(preset_name)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    results = {}
    formats = formats or ["design.md", "preview.html"]

    if "design.md" in [f.lower() for f in formats]:
        gen = DesignDocGenerator(preset=preset_name, output=str(out / "DESIGN.md"), lang="zh")
        gen.generate()
        results["DESIGN.md"] = str(out / "DESIGN.md")

    if "preview.html" in [f.lower() for f in formats]:
        preview_gen = PreviewGenerator(
            preset=preset_name,
            output=str(out / "preview.html"),
            title=f"{data.get('name', preset_name)} Preview",
        )
        preview_gen.generate()
        results["preview.html"] = str(out / "preview.html")

    if "css" in [f.lower() for f in formats]:
        exporter = DesignExporter(preset=preset_name, output_dir=str(out), formats=["css"])
        exporter.export()
        results["design-tokens.css"] = str(out / "design-tokens.css")

    if "json" in [f.lower() for f in formats]:
        tokens_path = out / "design-tokens.json"
        tokens_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
        results["design-tokens.json"] = str(tokens_path)

    return results
