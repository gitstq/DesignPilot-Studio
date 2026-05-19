#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Built-in Design Presets - Chinese product design systems
内置设计预设 - 中国顶级产品设计系统

Includes design tokens extracted from popular Chinese products:
- WeChat (微信)
- Alipay (支付宝)
- Feishu/Lark (飞书)
- Xiaohongshu (小红书)
- DingTalk (钉钉)
- Bilibili (B站)
- Taobao (淘宝)
- Douyin (抖音)
- Meituan (美团)
- Generic Modern (通用现代)
"""

from typing import Dict, Any, List


def get_all_presets() -> Dict[str, Dict[str, Any]]:
    """Return all built-in presets."""
    return {
        "wechat": _wechat_preset(),
        "alipay": _alipay_preset(),
        "feishu": _feishu_preset(),
        "xiaohongshu": _xiaohongshu_preset(),
        "dingtalk": _dingtalk_preset(),
        "bilibili": _bilibili_preset(),
        "taobao": _taobao_preset(),
        "douyin": _douyin_preset(),
        "meituan": _meituan_preset(),
        "modern": _modern_preset(),
    }


def get_preset(name: str) -> Dict[str, Any]:
    """Get a specific preset by name."""
    presets = get_all_presets()
    name_lower = name.lower().strip()
    if name_lower in presets:
        return presets[name_lower]
    # Fuzzy match
    for key, val in presets.items():
        if name_lower in key or key in name_lower:
            return val
    raise ValueError(f"Preset '{name}' not found. Available: {', '.join(presets.keys())}")


def list_presets() -> List[Dict[str, Any]]:
    """List all available presets with metadata."""
    presets = get_all_presets()
    result = []
    for name, preset in presets.items():
        tokens = preset.get("tokens", {})
        result.append({
            "name": name,
            "description": preset.get("description", ""),
            "category": preset.get("category", "general"),
            "tokens": tokens,
        })
    return result


def _wechat_preset() -> Dict[str, Any]:
    """WeChat (微信) design system - Clean, minimal, green-focused."""
    return {
        "name": "WeChat",
        "version": "1.0.0",
        "description": "微信设计系统 - 简洁、克制、绿色为主调的社交应用设计语言",
        "category": "social",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#07C160", "format": "hex", "description": "微信绿 - 品牌主色", "variants": {"light": "#38D976", "dark": "#06AD56"}, "usage": "按钮、链接、强调元素"},
                {"name": "secondary", "value": "#FA9D3B", "format": "hex", "description": "辅助橙 - 提示与高亮", "variants": {"light": "#FFB86C", "dark": "#E88B2F"}, "usage": "标签、徽章、次要操作"},
                {"name": "danger", "value": "#FA5151", "format": "hex", "description": "危险红 - 错误与警告", "variants": {"light": "#FF7979", "dark": "#E04545"}, "usage": "删除、错误提示、危险操作"},
                {"name": "warning", "value": "#FFC300", "format": "hex", "description": "警告黄 - 注意提醒", "variants": {"light": "#FFD54F", "dark": "#E6AF00"}, "usage": "警告提示、待处理状态"},
                {"name": "success", "value": "#07C160", "format": "hex", "description": "成功绿 - 完成确认", "variants": {"light": "#38D976", "dark": "#06AD56"}, "usage": "成功状态、完成标记"},
                {"name": "info", "value": "#10AEFF", "format": "hex", "description": "信息蓝 - 链接与引导", "variants": {"light": "#4DC4FF", "dark": "#0D9ADB"}, "usage": "信息提示、链接文字"},
                {"name": "bg-primary", "value": "#EDEDED", "format": "hex", "description": "主背景 - 浅灰", "variants": {"dark": "#111111"}, "usage": "页面主背景色"},
                {"name": "bg-secondary", "value": "#FFFFFF", "format": "hex", "description": "次背景 - 白色", "variants": {"dark": "#1A1A1A"}, "usage": "卡片、弹窗背景"},
                {"name": "text-primary", "value": "#191919", "format": "hex", "description": "主文字 - 深黑", "variants": {"dark": "#FFFFFF"}, "usage": "标题、重要文字"},
                {"name": "text-secondary", "value": "#999999", "format": "hex", "description": "次文字 - 灰色", "variants": {"dark": "#888888"}, "usage": "辅助说明、时间戳"},
                {"name": "text-placeholder", "value": "#CCCCCC", "format": "hex", "description": "占位文字 - 浅灰", "variants": {"dark": "#666666"}, "usage": "输入框占位符"},
                {"name": "border", "value": "#E5E5E5", "format": "hex", "description": "边框色", "variants": {"dark": "#333333"}, "usage": "分割线、边框"},
                {"name": "divider", "value": "#F0F0F0", "format": "hex", "description": "分割线", "variants": {"dark": "#2A2A2A"}, "usage": "列表分割线"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "20px", "weight": "600", "line_height": "1.4", "letter_spacing": "-0.02em", "description": "大标题", "usage": "页面标题"},
                {"name": "heading-lg", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "17px", "weight": "600", "line_height": "1.4", "letter_spacing": "-0.01em", "description": "中标题", "usage": "区块标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "15px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "小标题", "usage": "列表标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文", "usage": "主要内容文字"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字", "usage": "时间、标签、备注"},
                {"name": "micro", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "10px", "weight": "400", "line_height": "1.4", "letter_spacing": "0", "description": "极小文字", "usage": "角标、版权信息"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px", "description": "超小间距", "usage": "图标与文字间距"},
                {"name": "sm", "value": "8px", "description": "小间距", "usage": "紧凑元素间距"},
                {"name": "md", "value": "12px", "description": "中间距", "usage": "标准元素间距"},
                {"name": "lg", "value": "16px", "description": "大间距", "usage": "区块内间距"},
                {"name": "xl", "value": "24px", "description": "超大间距", "usage": "区块间间距"},
                {"name": "xxl", "value": "32px", "description": "特大间距", "usage": "页面级间距"},
                {"name": "page", "value": "16px", "description": "页面边距", "usage": "左右页面边距"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 2px rgba(0, 0, 0, 0.05)", "description": "小阴影", "usage": "轻微浮起效果"},
                {"name": "md", "value": "0 2px 8px rgba(0, 0, 0, 0.08)", "description": "中阴影", "usage": "卡片浮起效果"},
                {"name": "lg", "value": "0 4px 16px rgba(0, 0, 0, 0.12)", "description": "大阴影", "usage": "弹窗阴影"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px", "description": "小圆角", "usage": "按钮、标签"},
                {"name": "md", "value": "8px", "description": "中圆角", "usage": "卡片、输入框"},
                {"name": "lg", "value": "12px", "description": "大圆角", "usage": "弹窗、大卡片"},
                {"name": "full", "value": "9999px", "description": "全圆角", "usage": "头像、胶囊按钮"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px", "description": "iPhone SE"},
                {"name": "md", "value": "414px", "description": "iPhone Pro Max"},
                {"name": "lg", "value": "768px", "description": "iPad"},
                {"name": "xl", "value": "1024px", "description": "Desktop"},
            ],
            "animations": [
                {"name": "fast", "duration": "150ms", "easing": "ease-out", "description": "快速过渡", "usage": "按钮点击反馈"},
                {"name": "normal", "duration": "250ms", "easing": "ease-in-out", "description": "标准过渡", "usage": "页面切换"},
                {"name": "slow", "duration": "350ms", "easing": "cubic-bezier(0.4, 0, 0.2, 1)", "description": "慢速过渡", "usage": "弹窗动画"},
            ],
        },
        "metadata": {
            "brand": "WeChat",
            "brand_cn": "微信",
            "style": "Minimal, Clean, Functional",
            "style_cn": "简洁、克制、功能优先",
            "design_philosophy": "Less is more. Every pixel serves a purpose.",
            "ai_prompt_hint": "Build a clean, minimal mobile interface with green (#07C160) as the primary accent color. Use subtle shadows, rounded corners, and generous whitespace. Typography should use PingFang SC or system fonts.",
        },
    }


def _alipay_preset() -> Dict[str, Any]:
    """Alipay (支付宝) design system - Professional, trust-focused, blue."""
    return {
        "name": "Alipay",
        "version": "1.0.0",
        "description": "支付宝设计系统 - 专业、可信赖、蓝色主调的金融科技设计语言",
        "category": "fintech",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#1677FF", "format": "hex", "description": "支付宝蓝 - 品牌主色", "variants": {"light": "#4096FF", "dark": "#0958D9"}, "usage": "主按钮、链接、品牌标识"},
                {"name": "secondary", "value": "#FF6A00", "format": "hex", "description": "活力橙 - 支付与行动", "variants": {"light": "#FF8C33", "dark": "#E05E00"}, "usage": "支付按钮、促销标签"},
                {"name": "gold", "value": "#FAAD14", "format": "hex", "description": "金融金 - 财富与信任", "variants": {"light": "#FFC53D", "dark": "#D48806"}, "usage": "金融相关、会员标识"},
                {"name": "danger", "value": "#FF3141", "format": "hex", "description": "危险红", "variants": {"light": "#FF6370", "dark": "#CF1322"}, "usage": "错误、风险提示"},
                {"name": "success", "value": "#00B578", "format": "hex", "description": "成功绿", "variants": {"light": "#23C343", "dark": "#009A63"}, "usage": "交易成功、安全验证"},
                {"name": "bg-page", "value": "#F5F6FA", "format": "hex", "description": "页面背景", "variants": {"dark": "#141414"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#1F1F1F"}, "usage": "卡片、模块背景"},
                {"name": "text-primary", "value": "#1A1A1A", "format": "hex", "description": "主文字", "variants": {"dark": "#F0F0F0"}, "usage": "标题、重要信息"},
                {"name": "text-secondary", "value": "#86909C", "format": "hex", "description": "次文字", "variants": {"dark": "#A6A6A6"}, "usage": "辅助说明"},
                {"name": "text-disabled", "value": "#C9CDD4", "format": "hex", "description": "禁用文字", "variants": {"dark": "#595959"}, "usage": "禁用状态文字"},
                {"name": "border", "value": "#E5E6EB", "format": "hex", "description": "边框色", "variants": {"dark": "#434343"}, "usage": "分割线、边框"},
            ],
            "typography": [
                {"name": "display", "family": "'Alipay Number', 'DIN Alternate', -apple-system, sans-serif", "size": "32px", "weight": "700", "line_height": "1.2", "letter_spacing": "-0.02em", "description": "展示数字", "usage": "金额、数据展示"},
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "22px", "weight": "600", "line_height": "1.3", "letter_spacing": "-0.01em", "description": "大标题", "usage": "页面主标题"},
                {"name": "heading-lg", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "18px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "中标题", "usage": "区块标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "小标题", "usage": "卡片标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文", "usage": "主要内容"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字", "usage": "标签、备注"},
                {"name": "number", "family": "'Alipay Number', 'DIN Alternate', 'SF Mono', monospace", "size": "14px", "weight": "500", "line_height": "1.4", "letter_spacing": "0.02em", "description": "数字", "usage": "金额、数据"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px", "description": "超小间距"},
                {"name": "sm", "value": "8px", "description": "小间距"},
                {"name": "md", "value": "12px", "description": "中间距"},
                {"name": "lg", "value": "16px", "description": "大间距"},
                {"name": "xl", "value": "20px", "description": "超大间距"},
                {"name": "xxl", "value": "24px", "description": "特大间距"},
                {"name": "section", "value": "32px", "description": "区块间距"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 4px rgba(0, 0, 0, 0.06)", "description": "小阴影"},
                {"name": "md", "value": "0 2px 12px rgba(0, 0, 0, 0.08)", "description": "中阴影"},
                {"name": "lg", "value": "0 8px 24px rgba(0, 0, 0, 0.12)", "description": "大阴影"},
                {"name": "card", "value": "0 1px 0 0 #E5E6EB, 0 2px 8px rgba(0, 0, 0, 0.06)", "description": "卡片阴影"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px", "description": "小圆角"},
                {"name": "md", "value": "8px", "description": "中圆角"},
                {"name": "lg", "value": "12px", "description": "大圆角"},
                {"name": "xl", "value": "16px", "description": "超大圆角"},
                {"name": "full", "value": "9999px", "description": "全圆角"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px", "description": "Mobile S"},
                {"name": "md", "value": "414px", "description": "Mobile L"},
                {"name": "lg", "value": "768px", "description": "Tablet"},
                {"name": "xl", "value": "1024px", "description": "Desktop"},
                {"name": "xxl", "value": "1440px", "description": "Wide Desktop"},
            ],
            "animations": [
                {"name": "fast", "duration": "200ms", "easing": "ease-out", "description": "快速过渡"},
                {"name": "normal", "duration": "300ms", "easing": "ease-in-out", "description": "标准过渡"},
                {"name": "slow", "duration": "500ms", "easing": "cubic-bezier(0.4, 0, 0.2, 1)", "description": "慢速过渡"},
            ],
        },
        "metadata": {
            "brand": "Alipay",
            "brand_cn": "支付宝",
            "style": "Professional, Trustworthy, Data-driven",
            "style_cn": "专业、可信赖、数据驱动",
            "design_philosophy": "Trust through clarity. Every interaction reinforces security and reliability.",
            "ai_prompt_hint": "Build a professional fintech interface with blue (#1677FF) as the primary color and orange (#FF6A00) for action elements. Use DIN Alternate or similar fonts for numbers. Cards should have subtle shadows and clean borders. Prioritize data readability and trust signals.",
        },
    }


def _feishu_preset() -> Dict[str, Any]:
    """Feishu/Lark (飞书) design system - Efficient, vibrant, collaborative."""
    return {
        "name": "Feishu",
        "version": "1.0.0",
        "description": "飞书设计系统 - 高效、活力、协作优先的办公设计语言",
        "category": "productivity",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#3370FF", "format": "hex", "description": "飞书蓝 - 品牌主色", "variants": {"light": "#5E8FFF", "dark": "#245BDB"}, "usage": "主按钮、链接、选中态"},
                {"name": "secondary", "value": "#7C3AED", "format": "hex", "description": "协作紫", "variants": {"light": "#A78BFA", "dark": "#6D28D9"}, "usage": "协作功能、标签"},
                {"name": "accent", "value": "#14C4A0", "format": "hex", "description": "活力青", "variants": {"light": "#5EEAD4", "dark": "#0D9488"}, "usage": "在线状态、成功"},
                {"name": "danger", "value": "#F54A45", "format": "hex", "description": "警告红", "variants": {"light": "#F87171", "dark": "#DC2626"}, "usage": "错误、删除"},
                {"name": "warning", "value": "#FF9F18", "format": "hex", "description": "提醒橙", "variants": {"light": "#FBBF24", "dark": "#D97706"}, "usage": "警告提示"},
                {"name": "bg-page", "value": "#F5F6F7", "format": "hex", "description": "页面背景", "variants": {"dark": "#1E1F21"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#2C2E30"}, "usage": "卡片、面板"},
                {"name": "bg-hover", "value": "#F0F1F2", "format": "hex", "description": "悬停背景", "variants": {"dark": "#3A3C3E"}, "usage": "列表悬停"},
                {"name": "text-primary", "value": "#1F2329", "format": "hex", "description": "主文字", "variants": {"dark": "#E8E8E8"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#8F959E", "format": "hex", "description": "次文字", "variants": {"dark": "#A0A0A0"}, "usage": "辅助说明"},
                {"name": "border", "value": "#DEE0E3", "format": "hex", "description": "边框色", "variants": {"dark": "#48494B"}, "usage": "边框、分割线"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "24px", "weight": "600", "line_height": "1.3", "letter_spacing": "-0.02em", "description": "大标题", "usage": "页面标题"},
                {"name": "heading-lg", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "20px", "weight": "600", "line_height": "1.35", "letter_spacing": "-0.01em", "description": "中标题", "usage": "区块标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "小标题", "usage": "卡片标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文", "usage": "主要内容"},
                {"name": "body-sm", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "小正文", "usage": "辅助内容"},
                {"name": "code", "family": "'SF Mono', 'Fira Code', 'Consolas', monospace", "size": "13px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "代码字体", "usage": "代码块、等宽内容"},
            ],
            "spacing": [
                {"name": "compact", "value": "4px", "description": "紧凑间距"},
                {"name": "tight", "value": "8px", "description": "紧密间距"},
                {"name": "base", "value": "12px", "description": "基础间距"},
                {"name": "relaxed", "value": "16px", "description": "宽松间距"},
                {"name": "loose", "value": "24px", "description": "疏松间距"},
                {"name": "section", "value": "32px", "description": "区块间距"},
                {"name": "page", "value": "48px", "description": "页面间距"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 2px rgba(0, 0, 0, 0.04)", "description": "小阴影"},
                {"name": "md", "value": "0 4px 12px rgba(0, 0, 0, 0.08)", "description": "中阴影"},
                {"name": "lg", "value": "0 8px 24px rgba(0, 0, 0, 0.12)", "description": "大阴影"},
                {"name": "float", "value": "0 12px 32px rgba(0, 0, 0, 0.16)", "description": "浮层阴影"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px", "description": "小圆角"},
                {"name": "md", "value": "8px", "description": "中圆角"},
                {"name": "lg", "value": "12px", "description": "大圆角"},
                {"name": "xl", "value": "16px", "description": "超大圆角"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "480px", "description": "Mobile"},
                {"name": "md", "value": "768px", "description": "Tablet"},
                {"name": "lg", "value": "1024px", "description": "Desktop"},
                {"name": "xl", "value": "1440px", "description": "Wide"},
            ],
            "animations": [
                {"name": "fast", "duration": "150ms", "easing": "cubic-bezier(0.4, 0, 0.2, 1)", "description": "快速过渡"},
                {"name": "normal", "duration": "250ms", "easing": "cubic-bezier(0.4, 0, 0.2, 1)", "description": "标准过渡"},
                {"name": "slow", "duration": "400ms", "easing": "cubic-bezier(0.4, 0, 0.2, 1)", "description": "慢速过渡"},
            ],
        },
        "metadata": {
            "brand": "Feishu",
            "brand_cn": "飞书",
            "style": "Efficient, Vibrant, Collaborative",
            "style_cn": "高效、活力、协作优先",
            "design_philosophy": "Make work feel effortless. Every interaction should reduce cognitive load.",
            "ai_prompt_hint": "Build a modern productivity/SaaS interface with blue (#3370FF) as primary. Use clean card layouts, subtle hover states, and purple (#7C3AED) for collaborative features. Typography should be crisp and readable with good hierarchy.",
        },
    }


def _xiaohongshu_preset() -> Dict[str, Any]:
    """Xiaohongshu (小红书) design system - Lifestyle, warm, content-first."""
    return {
        "name": "Xiaohongshu",
        "version": "1.0.0",
        "description": "小红书设计系统 - 生活方式、温暖、内容优先的社区设计语言",
        "category": "lifestyle",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#FF2442", "format": "hex", "description": "小红书红 - 品牌主色", "variants": {"light": "#FF6B81", "dark": "#E0163A"}, "usage": "品牌标识、点赞、收藏"},
                {"name": "secondary", "value": "#FE2C55", "format": "hex", "description": "活力粉红", "variants": {"light": "#FF6B8A", "dark": "#E01E48"}, "usage": "标签、高亮"},
                {"name": "warm", "value": "#FF6B35", "format": "hex", "description": "温暖橙", "variants": {"light": "#FF8F5E", "dark": "#E55A25"}, "usage": "生活类标签"},
                {"name": "gold", "value": "#FFD700", "format": "hex", "description": "品质金", "variants": {"light": "#FFE44D", "dark": "#E6C200"}, "usage": "优质内容标识"},
                {"name": "bg-page", "value": "#F8F8F8", "format": "hex", "description": "页面背景", "variants": {"dark": "#111111"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#1A1A1A"}, "usage": "内容卡片"},
                {"name": "text-primary", "value": "#333333", "format": "hex", "description": "主文字", "variants": {"dark": "#EEEEEE"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#999999", "format": "hex", "description": "次文字", "variants": {"dark": "#888888"}, "usage": "辅助信息"},
                {"name": "border", "value": "#EEEEEE", "format": "hex", "description": "边框色", "variants": {"dark": "#333333"}, "usage": "分割线"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "20px", "weight": "700", "line_height": "1.3", "letter_spacing": "-0.01em", "description": "大标题", "usage": "笔记标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "中标题", "usage": "区块标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "14px", "weight": "400", "line_height": "1.7", "letter_spacing": "0", "description": "正文", "usage": "笔记内容"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字", "usage": "用户名、时间"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px", "description": "超小间距"},
                {"name": "sm", "value": "8px", "description": "小间距"},
                {"name": "md", "value": "12px", "description": "中间距"},
                {"name": "lg", "value": "16px", "description": "大间距"},
                {"name": "xl", "value": "24px", "description": "超大间距"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 4px rgba(0, 0, 0, 0.04)", "description": "小阴影"},
                {"name": "md", "value": "0 2px 12px rgba(0, 0, 0, 0.08)", "description": "中阴影"},
                {"name": "card", "value": "0 1px 6px rgba(0, 0, 0, 0.06)", "description": "卡片阴影"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px", "description": "小圆角"},
                {"name": "md", "value": "8px", "description": "中圆角"},
                {"name": "lg", "value": "12px", "description": "大圆角"},
                {"name": "card", "value": "16px", "description": "卡片圆角"},
                {"name": "full", "value": "9999px", "description": "全圆角"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px", "description": "Mobile"},
                {"name": "md", "value": "768px", "description": "Tablet"},
                {"name": "lg", "value": "1024px", "description": "Desktop"},
            ],
            "animations": [
                {"name": "fast", "duration": "200ms", "easing": "ease-out", "description": "快速过渡"},
                {"name": "normal", "duration": "300ms", "easing": "ease-in-out", "description": "标准过渡"},
                {"name": "like", "duration": "400ms", "easing": "cubic-bezier(0.175, 0.885, 0.32, 1.275)", "description": "点赞动画"},
            ],
        },
        "metadata": {
            "brand": "Xiaohongshu",
            "brand_cn": "小红书",
            "style": "Warm, Lifestyle, Content-first",
            "style_cn": "温暖、生活方式、内容优先",
            "design_philosophy": "Content is king. Design should enhance, never distract from user-generated content.",
            "ai_prompt_hint": "Build a lifestyle/social content platform with red (#FF2442) as the primary accent. Use warm tones, rounded cards with generous padding, and a waterfall/masonry layout for content cards. Images should be prominent with minimal text overlay.",
        },
    }


def _dingtalk_preset() -> Dict[str, Any]:
    """DingTalk (钉钉) design system - Enterprise, efficient, blue-white."""
    return {
        "name": "DingTalk",
        "version": "1.0.0",
        "description": "钉钉设计系统 - 企业级、高效、蓝白简洁的办公设计语言",
        "category": "enterprise",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#2F83FA", "format": "hex", "description": "钉钉蓝 - 品牌主色", "variants": {"light": "#5B9BF7", "dark": "#1A6DE0"}, "usage": "主按钮、链接"},
                {"name": "bg-page", "value": "#F2F3F5", "format": "hex", "description": "页面背景", "variants": {"dark": "#17171A"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#232324"}, "usage": "卡片、面板"},
                {"name": "text-primary", "value": "#17181A", "format": "hex", "description": "主文字", "variants": {"dark": "#F6F6F6"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#86909C", "format": "hex", "description": "次文字", "variants": {"dark": "#A6A6A6"}, "usage": "辅助说明"},
                {"name": "border", "value": "#E5E6EB", "format": "hex", "description": "边框色", "variants": {"dark": "#48494B"}, "usage": "边框、分割线"},
                {"name": "success", "value": "#00B42A", "format": "hex", "description": "成功绿", "usage": "成功状态"},
                {"name": "danger", "value": "#F53F3F", "format": "hex", "description": "危险红", "usage": "错误、删除"},
                {"name": "warning", "value": "#FF7D00", "format": "hex", "description": "警告橙", "usage": "警告提示"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "22px", "weight": "600", "line_height": "1.3", "letter_spacing": "-0.01em", "description": "大标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "中标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px"}, {"name": "sm", "value": "8px"},
                {"name": "md", "value": "12px"}, {"name": "lg", "value": "16px"},
                {"name": "xl", "value": "24px"}, {"name": "xxl", "value": "32px"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 4px rgba(0, 0, 0, 0.06)"},
                {"name": "md", "value": "0 4px 12px rgba(0, 0, 0, 0.08)"},
                {"name": "lg", "value": "0 8px 24px rgba(0, 0, 0, 0.12)"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px"}, {"name": "md", "value": "8px"},
                {"name": "lg", "value": "12px"}, {"name": "full", "value": "9999px"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px"}, {"name": "md", "value": "768px"},
                {"name": "lg", "value": "1024px"}, {"name": "xl", "value": "1440px"},
            ],
            "animations": [
                {"name": "fast", "duration": "150ms", "easing": "ease-out"},
                {"name": "normal", "duration": "250ms", "easing": "ease-in-out"},
            ],
        },
        "metadata": {
            "brand": "DingTalk",
            "brand_cn": "钉钉",
            "style": "Enterprise, Efficient, Structured",
            "style_cn": "企业级、高效、结构化",
            "design_philosophy": "Efficiency through structure. Clear hierarchy and predictable patterns.",
            "ai_prompt_hint": "Build an enterprise productivity tool with blue (#2F83FA) as primary. Use structured layouts, clear data tables, and a clean sidebar navigation. Prioritize information density and quick access to features.",
        },
    }


def _bilibili_preset() -> Dict[str, Any]:
    """Bilibili (B站) design system - Youthful, anime-inspired, pink-blue."""
    return {
        "name": "Bilibili",
        "version": "1.0.0",
        "description": "B站设计系统 - 年轻、二次元、粉蓝双色调的社区设计语言",
        "category": "entertainment",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#00A1D6", "format": "hex", "description": "B站蓝 - 品牌主色", "variants": {"light": "#33B8E0", "dark": "#0088B5"}, "usage": "主按钮、链接、品牌标识"},
                {"name": "secondary", "value": "#FB7299", "format": "hex", "description": "哔哩粉 - 社区色", "variants": {"light": "#FC9BB5", "dark": "#E55A82"}, "usage": "点赞、收藏、关注"},
                {"name": "accent", "value": "#23ADE5", "format": "hex", "description": "活力蓝", "variants": {"light": "#56C1EB", "dark": "#1B8FC0"}, "usage": "标签、高亮"},
                {"name": "warning", "value": "#FFB027", "format": "hex", "description": "提醒黄", "usage": "警告、硬币"},
                {"name": "bg-page", "value": "#F4F5F7", "format": "hex", "description": "页面背景", "variants": {"dark": "#17181A"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#212224"}, "usage": "卡片、视频封面"},
                {"name": "text-primary", "value": "#18191C", "format": "hex", "description": "主文字", "variants": {"dark": "#E6E6E6"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#9499A0", "format": "hex", "description": "次文字", "variants": {"dark": "#999999"}, "usage": "播放量、时间"},
                {"name": "border", "value": "#E3E5E7", "format": "hex", "description": "边框色", "variants": {"dark": "#3B3C3E"}, "usage": "分割线、边框"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "20px", "weight": "600", "line_height": "1.3", "letter_spacing": "-0.01em", "description": "大标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "中标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px"}, {"name": "sm", "value": "8px"},
                {"name": "md", "value": "12px"}, {"name": "lg", "value": "16px"},
                {"name": "xl", "value": "24px"}, {"name": "xxl", "value": "32px"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 2px rgba(0, 0, 0, 0.04)"},
                {"name": "md", "value": "0 4px 12px rgba(0, 0, 0, 0.08)"},
                {"name": "card", "value": "0 1px 4px rgba(0, 0, 0, 0.06)"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px"}, {"name": "md", "value": "6px"},
                {"name": "lg", "value": "8px"}, {"name": "card", "value": "10px"},
                {"name": "full", "value": "9999px"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px"}, {"name": "md", "value": "768px"},
                {"name": "lg", "value": "1024px"}, {"name": "xl", "value": "1440px"},
            ],
            "animations": [
                {"name": "fast", "duration": "200ms", "easing": "ease-out"},
                {"name": "normal", "duration": "300ms", "easing": "ease-in-out"},
                {"name": "danmaku", "duration": "5000ms", "easing": "linear", "description": "弹幕动画"},
            ],
        },
        "metadata": {
            "brand": "Bilibili",
            "brand_cn": "B站",
            "style": "Youthful, Playful, Community-driven",
            "style_cn": "年轻、活泼、社区驱动",
            "design_philosophy": "Fun meets function. Design should spark joy and encourage interaction.",
            "ai_prompt_hint": "Build a youthful video/content community platform with blue (#00A1D6) and pink (#FB7299) as the dual accent colors. Use rounded cards, playful hover effects, and a video-centric grid layout. Include danmaku (bullet comment) style overlays.",
        },
    }


def _taobao_preset() -> Dict[str, Any]:
    """Taobao (淘宝) design system - Commerce, vibrant, conversion-focused."""
    return {
        "name": "Taobao",
        "version": "1.0.0",
        "description": "淘宝设计系统 - 电商、活力、转化导向的购物设计语言",
        "category": "ecommerce",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#FF5000", "format": "hex", "description": "淘宝橙 - 品牌主色", "variants": {"light": "#FF7733", "dark": "#E04600"}, "usage": "主按钮、价格、促销"},
                {"name": "secondary", "value": "#FF2D4B", "format": "hex", "description": "促销红", "variants": {"light": "#FF5C72", "dark": "#E0253F"}, "usage": "促销标签、限时"},
                {"name": "gold", "value": "#FF9900", "format": "hex", "description": "品质金", "variants": {"light": "#FFB333", "dark": "#E08800"}, "usage": "会员、品质"},
                {"name": "success", "value": "#00C853", "format": "hex", "description": "成功绿", "usage": "交易成功"},
                {"name": "bg-page", "value": "#F5F5F5", "format": "hex", "description": "页面背景", "variants": {"dark": "#121212"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#1E1E1E"}, "usage": "商品卡片"},
                {"name": "text-primary", "value": "#222222", "format": "hex", "description": "主文字", "variants": {"dark": "#EEEEEE"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#999999", "format": "hex", "description": "次文字", "variants": {"dark": "#888888"}, "usage": "辅助信息"},
                {"name": "price", "value": "#FF2D4B", "format": "hex", "description": "价格红", "usage": "商品价格"},
                {"name": "border", "value": "#EEEEEE", "format": "hex", "description": "边框色", "variants": {"dark": "#333333"}, "usage": "分割线"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "20px", "weight": "700", "line_height": "1.3", "letter_spacing": "0", "description": "大标题"},
                {"name": "price-lg", "family": "'DIN Alternate', 'Helvetica Neue', sans-serif", "size": "24px", "weight": "700", "line_height": "1.2", "letter_spacing": "-0.02em", "description": "大价格", "usage": "商品价格"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px"}, {"name": "sm", "value": "8px"},
                {"name": "md", "value": "12px"}, {"name": "lg", "value": "16px"},
                {"name": "xl", "value": "24px"}, {"name": "xxl", "value": "32px"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 4px rgba(0, 0, 0, 0.05)"},
                {"name": "md", "value": "0 4px 12px rgba(0, 0, 0, 0.08)"},
                {"name": "card", "value": "0 2px 8px rgba(0, 0, 0, 0.06)"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px"}, {"name": "md", "value": "8px"},
                {"name": "lg", "value": "12px"}, {"name": "card", "value": "16px"},
                {"name": "full", "value": "9999px"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px"}, {"name": "md", "value": "768px"},
                {"name": "lg", "value": "1024px"}, {"name": "xl", "value": "1440px"},
            ],
            "animations": [
                {"name": "fast", "duration": "200ms", "easing": "ease-out"},
                {"name": "normal", "duration": "300ms", "easing": "ease-in-out"},
                {"name": "bounce", "duration": "500ms", "easing": "cubic-bezier(0.68, -0.55, 0.265, 1.55)", "description": "弹跳动画"},
            ],
        },
        "metadata": {
            "brand": "Taobao",
            "brand_cn": "淘宝",
            "style": "Vibrant, Conversion-focused, Commerce",
            "style_cn": "活力、转化导向、电商",
            "design_philosophy": "Every pixel drives conversion. Design should guide users from browsing to buying.",
            "ai_prompt_hint": "Build an e-commerce shopping platform with orange (#FF5000) as primary and red (#FF2D4B) for prices/promotions. Use product card grids, prominent price displays in bold DIN font, and clear call-to-action buttons. Warm, inviting color palette.",
        },
    }


def _douyin_preset() -> Dict[str, Any]:
    """Douyin (抖音) design system - Trendy, dark, immersive."""
    return {
        "name": "Douyin",
        "version": "1.0.0",
        "description": "抖音设计系统 - 潮流、沉浸、深色为主的短视频设计语言",
        "category": "entertainment",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#FE2C55", "format": "hex", "description": "抖音红 - 品牌主色", "variants": {"light": "#FF5C78", "dark": "#E02048"}, "usage": "点赞、关注、品牌标识"},
                {"name": "secondary", "value": "#25F4EE", "format": "hex", "description": "抖音青", "variants": {"light": "#5CF7F1", "dark": "#1DD4CC"}, "usage": "特效、分享"},
                {"name": "gradient-start", "value": "#FE2C55", "format": "hex", "description": "渐变起始色", "usage": "品牌渐变"},
                {"name": "gradient-end", "value": "#25F4EE", "format": "hex", "description": "渐变结束色", "usage": "品牌渐变"},
                {"name": "bg-page", "value": "#121212", "format": "hex", "description": "页面背景（深色）", "usage": "页面主背景"},
                {"name": "bg-card", "value": "#1E1E1E", "format": "hex", "description": "卡片背景", "usage": "弹窗、面板"},
                {"name": "text-primary", "value": "#FFFFFF", "format": "hex", "description": "主文字（白色）", "usage": "标题、正文"},
                {"name": "text-secondary", "value": "rgba(255, 255, 255, 0.6)", "format": "hex", "description": "次文字", "usage": "辅助信息"},
                {"name": "text-tertiary", "value": "rgba(255, 255, 255, 0.4)", "format": "hex", "description": "三级文字", "usage": "时间戳"},
                {"name": "overlay", "value": "rgba(0, 0, 0, 0.6)", "format": "hex", "description": "遮罩层", "usage": "弹窗遮罩"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "18px", "weight": "700", "line_height": "1.3", "letter_spacing": "0", "description": "大标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "15px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "中标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "14px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "正文"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "12px", "weight": "400", "line_height": "1.4", "letter_spacing": "0", "description": "辅助文字"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px"}, {"name": "sm", "value": "8px"},
                {"name": "md", "value": "12px"}, {"name": "lg", "value": "16px"},
                {"name": "xl", "value": "24px"},
            ],
            "shadows": [
                {"name": "glow-red", "value": "0 0 20px rgba(254, 44, 85, 0.3)", "description": "红色光晕"},
                {"name": "glow-cyan", "value": "0 0 20px rgba(37, 244, 238, 0.3)", "description": "青色光晕"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px"}, {"name": "md", "value": "8px"},
                {"name": "lg", "value": "12px"}, {"name": "full", "value": "9999px"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px"}, {"name": "md", "value": "414px"},
                {"name": "lg", "value": "768px"},
            ],
            "animations": [
                {"name": "fast", "duration": "200ms", "easing": "ease-out"},
                {"name": "heart", "duration": "600ms", "easing": "cubic-bezier(0.175, 0.885, 0.32, 1.275)", "description": "点赞心跳"},
                {"name": "slide-up", "duration": "350ms", "easing": "cubic-bezier(0.4, 0, 0.2, 1)", "description": "底部弹出"},
            ],
        },
        "metadata": {
            "brand": "Douyin",
            "brand_cn": "抖音",
            "style": "Immersive, Dark, Trendy",
            "style_cn": "沉浸、深色、潮流",
            "design_philosophy": "Content fills the screen. UI gets out of the way.",
            "ai_prompt_hint": "Build a dark-themed short video app with red (#FE2C55) and cyan (#25F4EE) as dual accent colors. Full-screen immersive layout, bottom navigation, side action buttons (like, comment, share). Use glassmorphism effects and gradient accents.",
        },
    }


def _meituan_preset() -> Dict[str, Any]:
    """Meituan (美团) design system - Local services, warm yellow, practical."""
    return {
        "name": "Meituan",
        "version": "1.0.0",
        "description": "美团设计系统 - 本地生活、温暖黄调、实用导向的设计语言",
        "category": "lifestyle",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#FFC300", "format": "hex", "description": "美团黄 - 品牌主色", "variants": {"light": "#FFD54F", "dark": "#FFB000"}, "usage": "品牌标识、评分"},
                {"name": "secondary", "value": "#FF6633", "format": "hex", "description": "外卖橙", "variants": {"light": "#FF8855", "dark": "#E05522"}, "usage": "外卖、配送"},
                {"name": "success", "value": "#06B05C", "format": "hex", "description": "成功绿", "usage": "营业中、好评"},
                {"name": "danger", "value": "#F5222D", "format": "hex", "description": "危险红", "usage": "已打烊、差评"},
                {"name": "bg-page", "value": "#F5F5F5", "format": "hex", "description": "页面背景", "variants": {"dark": "#141414"}, "usage": "页面主背景"},
                {"name": "bg-card", "value": "#FFFFFF", "format": "hex", "description": "卡片背景", "variants": {"dark": "#1F1F1F"}, "usage": "卡片、弹窗"},
                {"name": "text-primary", "value": "#333333", "format": "hex", "description": "主文字", "variants": {"dark": "#F0F0F0"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#999999", "format": "hex", "description": "次文字", "variants": {"dark": "#888888"}, "usage": "辅助信息"},
                {"name": "border", "value": "#E8E8E8", "format": "hex", "description": "边框色", "variants": {"dark": "#333333"}, "usage": "分割线"},
            ],
            "typography": [
                {"name": "heading-xl", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "20px", "weight": "700", "line_height": "1.3", "letter_spacing": "0", "description": "大标题"},
                {"name": "heading-md", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "中标题"},
                {"name": "body", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文"},
                {"name": "caption", "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif", "size": "12px", "weight": "400", "line_height": "1.5", "letter_spacing": "0", "description": "辅助文字"},
            ],
            "spacing": [
                {"name": "xs", "value": "4px"}, {"name": "sm", "value": "8px"},
                {"name": "md", "value": "12px"}, {"name": "lg", "value": "16px"},
                {"name": "xl", "value": "24px"},
            ],
            "shadows": [
                {"name": "sm", "value": "0 1px 4px rgba(0, 0, 0, 0.05)"},
                {"name": "md", "value": "0 2px 12px rgba(0, 0, 0, 0.08)"},
            ],
            "borderRadius": [
                {"name": "sm", "value": "4px"}, {"name": "md", "value": "8px"},
                {"name": "lg", "value": "12px"}, {"name": "full", "value": "9999px"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "375px"}, {"name": "md", "value": "768px"},
                {"name": "lg", "value": "1024px"},
            ],
            "animations": [
                {"name": "fast", "duration": "200ms", "easing": "ease-out"},
                {"name": "normal", "duration": "300ms", "easing": "ease-in-out"},
            ],
        },
        "metadata": {
            "brand": "Meituan",
            "brand_cn": "美团",
            "style": "Warm, Practical, Service-oriented",
            "style_cn": "温暖、实用、服务导向",
            "design_philosophy": "Local life at your fingertips. Design should feel warm and accessible.",
            "ai_prompt_hint": "Build a local services app with warm yellow (#FFC300) as primary and orange (#FF6633) for delivery features. Use card-based layouts for restaurants/shops, prominent star ratings, and clear category icons. Warm and inviting color palette.",
        },
    }


def _modern_preset() -> Dict[str, Any]:
    """Generic modern design system - Clean, versatile, well-balanced."""
    return {
        "name": "Modern",
        "version": "1.0.0",
        "description": "通用现代设计系统 - 简洁、通用、平衡的现代设计语言",
        "category": "general",
        "author": "DesignPilot",
        "tokens": {
            "colors": [
                {"name": "primary", "value": "#6366F1", "format": "hex", "description": "主色 - Indigo", "variants": {"50": "#EEF2FF", "100": "#E0E7FF", "200": "#C7D2FE", "300": "#A5B4FC", "400": "#818CF8", "500": "#6366F1", "600": "#4F46E5", "700": "#4338CA", "800": "#3730A3", "900": "#312E81"}, "usage": "主按钮、链接、品牌色"},
                {"name": "secondary", "value": "#8B5CF6", "format": "hex", "description": "辅助色 - Violet", "variants": {"light": "#A78BFA", "dark": "#7C3AED"}, "usage": "辅助元素"},
                {"name": "success", "value": "#22C55E", "format": "hex", "description": "成功色", "variants": {"light": "#4ADE80", "dark": "#16A34A"}, "usage": "成功状态"},
                {"name": "warning", "value": "#F59E0B", "format": "hex", "description": "警告色", "variants": {"light": "#FBBF24", "dark": "#D97706"}, "usage": "警告提示"},
                {"name": "danger", "value": "#EF4444", "format": "hex", "description": "危险色", "variants": {"light": "#F87171", "dark": "#DC2626"}, "usage": "错误、删除"},
                {"name": "info", "value": "#3B82F6", "format": "hex", "description": "信息色", "variants": {"light": "#60A5FA", "dark": "#2563EB"}, "usage": "信息提示"},
                {"name": "bg-primary", "value": "#FFFFFF", "format": "hex", "description": "主背景", "variants": {"dark": "#0F172A"}, "usage": "页面背景"},
                {"name": "bg-secondary", "value": "#F8FAFC", "format": "hex", "description": "次背景", "variants": {"dark": "#1E293B"}, "usage": "区块背景"},
                {"name": "text-primary", "value": "#0F172A", "format": "hex", "description": "主文字", "variants": {"dark": "#F8FAFC"}, "usage": "标题、正文"},
                {"name": "text-secondary", "value": "#64748B", "format": "hex", "description": "次文字", "variants": {"dark": "#94A3B8"}, "usage": "辅助说明"},
                {"name": "border", "value": "#E2E8F0", "format": "hex", "description": "边框色", "variants": {"dark": "#334155"}, "usage": "边框、分割线"},
            ],
            "typography": [
                {"name": "display", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "36px", "weight": "800", "line_height": "1.1", "letter_spacing": "-0.03em", "description": "展示标题", "usage": "Hero区域"},
                {"name": "heading-xl", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "24px", "weight": "700", "line_height": "1.25", "letter_spacing": "-0.02em", "description": "大标题", "usage": "页面标题"},
                {"name": "heading-lg", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "20px", "weight": "600", "line_height": "1.3", "letter_spacing": "-0.01em", "description": "中标题", "usage": "区块标题"},
                {"name": "heading-md", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "16px", "weight": "600", "line_height": "1.4", "letter_spacing": "0", "description": "小标题", "usage": "卡片标题"},
                {"name": "body-lg", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "16px", "weight": "400", "line_height": "1.7", "letter_spacing": "0", "description": "大正文", "usage": "主要内容"},
                {"name": "body", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "正文", "usage": "标准正文"},
                {"name": "caption", "family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", "size": "12px", "weight": "500", "line_height": "1.5", "letter_spacing": "0.02em", "description": "辅助文字", "usage": "标签、备注"},
                {"name": "mono", "family": "'JetBrains Mono', 'Fira Code', 'SF Mono', monospace", "size": "14px", "weight": "400", "line_height": "1.6", "letter_spacing": "0", "description": "等宽字体", "usage": "代码块"},
            ],
            "spacing": [
                {"name": "0", "value": "0px", "description": "无间距"},
                {"name": "px", "value": "1px", "description": "1像素"},
                {"name": "0.5", "value": "2px", "description": "0.5x"},
                {"name": "1", "value": "4px", "description": "1x 基础单位"},
                {"name": "1.5", "value": "6px", "description": "1.5x"},
                {"name": "2", "value": "8px", "description": "2x"},
                {"name": "3", "value": "12px", "description": "3x"},
                {"name": "4", "value": "16px", "description": "4x"},
                {"name": "5", "value": "20px", "description": "5x"},
                {"name": "6", "value": "24px", "description": "6x"},
                {"name": "8", "value": "32px", "description": "8x"},
                {"name": "10", "value": "40px", "description": "10x"},
                {"name": "12", "value": "48px", "description": "12x"},
                {"name": "16", "value": "64px", "description": "16x"},
                {"name": "20", "value": "80px", "description": "20x"},
                {"name": "24", "value": "96px", "description": "24x"},
            ],
            "shadows": [
                {"name": "xs", "value": "0 1px 2px rgba(0, 0, 0, 0.05)", "description": "极小阴影"},
                {"name": "sm", "value": "0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06)", "description": "小阴影"},
                {"name": "md", "value": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)", "description": "中阴影"},
                {"name": "lg", "value": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)", "description": "大阴影"},
                {"name": "xl", "value": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)", "description": "超大阴影"},
                {"name": "inner", "value": "inset 0 2px 4px rgba(0, 0, 0, 0.06)", "description": "内阴影"},
            ],
            "borderRadius": [
                {"name": "none", "value": "0px", "description": "无圆角"},
                {"name": "sm", "value": "2px", "description": "小圆角"},
                {"name": "md", "value": "6px", "description": "中圆角"},
                {"name": "lg", "value": "8px", "description": "大圆角"},
                {"name": "xl", "value": "12px", "description": "超大圆角"},
                {"name": "2xl", "value": "16px", "description": "2xl圆角"},
                {"name": "3xl", "value": "24px", "description": "3xl圆角"},
                {"name": "full", "value": "9999px", "description": "全圆角"},
            ],
            "breakpoints": [
                {"name": "sm", "value": "640px", "description": "Small devices"},
                {"name": "md", "value": "768px", "description": "Medium devices"},
                {"name": "lg", "value": "1024px", "description": "Large devices"},
                {"name": "xl", "value": "1280px", "description": "Extra large"},
                {"name": "2xl", "value": "1536px", "description": "2X Extra large"},
            ],
            "animations": [
                {"name": "fast", "duration": "100ms", "easing": "ease-out", "description": "快速过渡"},
                {"name": "normal", "duration": "200ms", "easing": "ease-in-out", "description": "标准过渡"},
                {"name": "slow", "duration": "300ms", "easing": "ease-in-out", "description": "慢速过渡"},
                {"name": "spring", "duration": "500ms", "easing": "cubic-bezier(0.34, 1.56, 0.64, 1)", "description": "弹性动画"},
            ],
        },
        "metadata": {
            "brand": "Modern",
            "brand_cn": "通用现代",
            "style": "Clean, Versatile, Well-balanced",
            "style_cn": "简洁、通用、平衡",
            "design_philosophy": "Timeless design that works across all contexts. Balance beauty with function.",
            "ai_prompt_hint": "Build a clean modern web application with indigo (#6366F1) as the primary color. Use a 4px base spacing grid, subtle shadows, and Inter font family. Cards should have 8px border radius and gentle hover effects. Light, airy feel with good whitespace.",
        },
    }
