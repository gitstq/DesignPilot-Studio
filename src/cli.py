#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DesignPilot CLI - Main entry point
DesignPilot 命令行入口

Usage:
    python -m src.cli init          # Initialize a new design system project
    python -m src.cli extract       # Extract design tokens from CSS/HTML
    python -m src.cli generate      # Generate DESIGN.md from tokens
    python -m src.cli preview       # Generate interactive HTML preview
    python -m src.cli export        # Export to CSS/JSON/Tailwind formats
    python -m src.cli list          # List available presets
    python -m src.cli apply         # Apply a preset to current project
    python -m src.cli validate      # Validate design system consistency
"""

import sys
import os
import argparse
import json
import textwrap
from pathlib import Path
from typing import Optional, List, Dict, Any


def print_banner():
    """Print DesignPilot ASCII banner."""
    banner = r"""
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║   🎨  DesignPilot v1.0.0                             ║
    ║   Lightweight AI Design System Extraction Engine     ║
    ║   轻量级AI设计系统提取与可视化引擎                     ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)


def cmd_init(args):
    """Initialize a new design system project."""
    from .project import init_project
    name = args.name or "my-design-system"
    output_dir = args.output or "."
    preset = args.preset
    init_project(name=name, output_dir=output_dir, preset=preset)


def cmd_extract(args):
    """Extract design tokens from source files."""
    from .extractor import DesignExtractor
    extractor = DesignExtractor(
        source=args.source,
        output=args.output,
        format=args.format,
        url=args.url,
    )
    result = extractor.extract()
    print(f"✅ Extracted {len(result.get('colors', []))} colors, "
          f"{len(result.get('typography', []))} typography tokens, "
          f"{len(result.get('spacing', []))} spacing tokens")
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"📁 Saved to {out_path}")


def cmd_generate(args):
    """Generate DESIGN.md from tokens or preset."""
    from .generator import DesignDocGenerator
    generator = DesignDocGenerator(
        input_file=args.input,
        output=args.output,
        preset=args.preset,
        lang=args.lang,
        include_preview=args.preview,
    )
    output_path = generator.generate()
    print(f"📄 Generated DESIGN.md at: {output_path}")


def cmd_preview(args):
    """Generate interactive HTML preview."""
    from .preview import PreviewGenerator
    preview_gen = PreviewGenerator(
        input_file=args.input,
        output=args.output,
        preset=args.preset,
        theme=args.theme,
        title=args.title,
    )
    output_path = preview_gen.generate()
    print(f"🎨 Generated preview at: {output_path}")
    print(f"💡 Open in browser: file://{output_path}")


def cmd_export(args):
    """Export design tokens to various formats."""
    from .exporter import DesignExporter
    exporter = DesignExporter(
        input_file=args.input,
        output_dir=args.output or ".",
        formats=args.formats,
        preset=args.preset,
    )
    results = exporter.export()
    for fmt, path in results.items():
        print(f"📦 Exported {fmt}: {path}")


def cmd_list(args):
    """List available presets."""
    from .presets import list_presets
    presets = list_presets()
    if not presets:
        print("📋 No presets found.")
        return
    print(f"📋 Available presets ({len(presets)}):\n")
    for p in presets:
        print(f"  🎨 {p['name']}")
        print(f"     {p.get('description', 'No description')}")
        print(f"     Category: {p.get('category', 'general')}")
        print(f"     Colors: {len(p.get('tokens', {}).get('colors', []))} | "
              f"Typography: {len(p.get('tokens', {}).get('typography', []))} | "
              f"Spacing: {len(p.get('tokens', {}).get('spacing', []))}")
        print()


def cmd_apply(args):
    """Apply a preset to current project."""
    from .presets import apply_preset
    result = apply_preset(
        preset_name=args.preset,
        output_dir=args.output or ".",
        formats=args.formats or ["design.md", "preview.html"],
    )
    for fmt, path in result.items():
        print(f"✅ Applied {fmt}: {path}")


def cmd_validate(args):
    """Validate design system consistency."""
    from .validator import DesignValidator
    validator = DesignValidator(input_file=args.input)
    report = validator.validate()
    validator.print_report(report)
    if report['score'] >= 80:
        print(f"\n✅ Design system score: {report['score']}/100 - Good!")
    elif report['score'] >= 60:
        print(f"\n⚠️  Design system score: {report['score']}/100 - Needs improvement")
    else:
        print(f"\n❌ Design system score: {report['score']}/100 - Significant issues found")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="designpilot",
        description="🎨 DesignPilot - Lightweight AI Design System Extraction & Visualization Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          designpilot init --name my-app --preset wechat
          designpilot extract --source styles.css --output tokens.json
          designpilot generate --preset alipay --lang zh
          designpilot preview --preset feishu --theme dark
          designpilot export --input tokens.json --formats css json tailwind
          designpilot list
          designpilot validate --input DESIGN.md
        """),
    )
    parser.add_argument('-v', '--version', action='version', version='DesignPilot v1.0.0')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # init
    p_init = subparsers.add_parser('init', help='Initialize a new design system project')
    p_init.add_argument('-n', '--name', help='Project name')
    p_init.add_argument('-o', '--output', help='Output directory')
    p_init.add_argument('-p', '--preset', help='Apply a preset during init')

    # extract
    p_extract = subparsers.add_parser('extract', help='Extract design tokens from source files')
    p_extract.add_argument('-s', '--source', help='Source CSS/HTML file path')
    p_extract.add_argument('-o', '--output', help='Output JSON file path')
    p_extract.add_argument('-f', '--format', default='css', choices=['css', 'html', 'auto'],
                           help='Source format (default: css)')
    p_extract.add_argument('-u', '--url', help='URL to extract from (requires network)')

    # generate
    p_gen = subparsers.add_parser('generate', help='Generate DESIGN.md from tokens or preset')
    p_gen.add_argument('-i', '--input', help='Input tokens JSON file')
    p_gen.add_argument('-o', '--output', default='DESIGN.md', help='Output file path')
    p_gen.add_argument('-p', '--preset', help='Use a built-in preset')
    p_gen.add_argument('-l', '--lang', default='zh', choices=['zh', 'en', 'ja'],
                       help='Documentation language')
    p_gen.add_argument('--preview', action='store_true', help='Include preview code blocks')

    # preview
    p_preview = subparsers.add_parser('preview', help='Generate interactive HTML preview')
    p_preview.add_argument('-i', '--input', help='Input tokens JSON file')
    p_preview.add_argument('-o', '--output', default='preview.html', help='Output HTML file')
    p_preview.add_argument('-p', '--preset', help='Use a built-in preset')
    p_preview.add_argument('-t', '--theme', default='light', choices=['light', 'dark', 'both'],
                           help='Preview theme')
    p_preview.add_argument('--title', help='Preview page title')

    # export
    p_export = subparsers.add_parser('export', help='Export design tokens to various formats')
    p_export.add_argument('-i', '--input', help='Input tokens JSON file')
    p_export.add_argument('-o', '--output', help='Output directory')
    p_export.add_argument('-f', '--formats', nargs='+',
                          default=['css', 'json'],
                          choices=['css', 'json', 'tailwind', 'scss', 'less'],
                          help='Export formats')
    p_export.add_argument('-p', '--preset', help='Use a built-in preset')

    # list
    subparsers.add_parser('list', help='List available presets')

    # apply
    p_apply = subparsers.add_parser('apply', help='Apply a preset to current project')
    p_apply.add_argument('preset', help='Preset name to apply')
    p_apply.add_argument('-o', '--output', help='Output directory')
    p_apply.add_argument('-f', '--formats', nargs='+', help='Output formats')

    # validate
    p_validate = subparsers.add_parser('validate', help='Validate design system consistency')
    p_validate.add_argument('-i', '--input', help='Input DESIGN.md or tokens JSON file')

    args = parser.parse_args()

    if not args.command:
        print_banner()
        parser.print_help()
        return

    print_banner()

    command_map = {
        'init': cmd_init,
        'extract': cmd_extract,
        'generate': cmd_generate,
        'preview': cmd_preview,
        'export': cmd_export,
        'list': cmd_list,
        'apply': cmd_apply,
        'validate': cmd_validate,
    }

    handler = command_map.get(args.command)
    if handler:
        try:
            handler(args)
        except KeyboardInterrupt:
            print("\n\n👋 Operation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
