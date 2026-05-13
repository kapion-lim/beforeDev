---
name: project-builder
description: |
  一键生成项目需求文档、流程图、Axure原型规范、页面跳转映射表、HTML可交互原型及UI设计稿的技能。当用户需要创建新项目、编写需求文档、设计产品原型、规划业务流程、制作可交互原型时使用此技能。支持：
  (1) 生成结构化的 Markdown 需求文档
  (2) 创建详细的业务流程图和交互流程图（Mermaid语法）
  (3) 生成 Axure RP 原型设计规范（含页面结构、交互说明、组件库）
  (4) 生成详细的页面跳转映射表（含跳转矩阵、参数规范、埋点规范）
  (5) 生成可运行的 HTML 原型（含完整 CSS/JS，假数据丰富页面，支持交互操作）
  (6) 生成高保真 UI 设计稿（线框图 + UI 设计稿）
  触发场景：创建项目、生成需求文档、设计流程图、做产品原型、生成设计稿、项目规划、Axure原型、交互设计、HTML原型等。
---

# Project Builder V9 (Final)

一键生成项目需求文档、流程图、Axure原型规范、HTML可交互原型及UI设计稿。

---

## 🎯 工作流程（含步骤确认）

### 步骤1️⃣：需求收集与确认

**目的**：明确项目需求和范围

**操作**：
1. 提取项目信息：项目名称、核心功能、用户角色、使用场景
2. 使用 `AskUserQuestion` 确认：
   - 项目类型（电商/社交/工具/内容/其他）
   - 目标平台（移动端/Web/小程序）
   - 核心功能优先级

**输出**：确认后的需求清单

---

### 步骤2️⃣：设计风格确认 ⭐⭐⭐

**目的**：确保原型视觉风格符合用户期望，避免返工

**操作**：使用 `AskUserQuestion` 让用户选择设计风格

#### 设计风格选项：

| 风格 | 特点 | 主色调 | 适用场景 | 参考APP |
|------|------|--------|---------|---------|
| **现代电商风** | 活力橙红、精致卡片、流畅动效 | #ff4757 橙红 | 电商、零售、团购 | 淘宝、京东、拼多多 |
| **简约扁平风** | 紫蓝渐变、大量留白、简洁线条 | #667eea 紫蓝 | 工具类、企业应用 | Notion、飞书 |
| **暗黑高端风** | 深色背景、金色点缀、精致细节 | #1a1a2e 深色 | 奢侈品、会员应用 | Apple Store、得物 |
| **清新自然风** | 绿/蓝色系、圆润设计、柔和配色 | #34c759 绿色 | 生活服务、健康应用 | 美团、饿了么 |
| **社交活力风** | 粉紫渐变、年轻化、互动感强 | #ff2d55 粉红 | 社交、内容社区 | 小红书、抖音 |

#### 主色调选项：

| 配色 | 色值 | 氛围 |
|------|------|------|
| 活力橙红 | #ff4757 | 热情、促销、购买欲 |
| 紫蓝渐变 | #667eea → #764ba2 | 科技、现代、专业 |
| 清新绿色 | #34c759 | 自然、健康、环保 |
| 粉紫渐变 | #ff2d55 → #5856d6 | 年轻、活力、社交 |
| 金色奢华 | #ffd700 → #ffb800 | 高端、会员、品质 |

**输出**：用户选择的设计风格配置（风格+主色调）

---

### 步骤3️⃣：设计参考确认 ⭐⭐

**目的**：提供视觉参考（文字+图片），确保设计方向正确

**操作**：
1. **生成设计参考图片** - 使用 `GenerateImage` 生成用户选择风格的参考图
2. **展示设计说明** - 文字描述设计细节
3. **用户确认** - 使用 `AskUserQuestion` 让用户确认或调整

#### 生成设计参考图片：

根据用户选择的风格，生成对应的设计参考图：

```python
# 现代电商风参考图
GenerateImage(
    prompt="Mobile e-commerce app UI design reference, vibrant coral-red theme (#ff4757), clean white background, product cards with rounded corners, search bar at top, banner carousel, category icons grid, flash sale section, modern minimalist style, professional UI mockup, high quality, distinctive visual character",
    path="{workspace}/assets/design-reference-modern-ecommerce.png",
    image_size="landscape_16_9"
)

# 简约扁平风参考图
GenerateImage(
    prompt="Minimalist flat design UI reference, purple-blue gradient (#667eea), lots of white space, clean lines, simple card layout, professional tool app interface, modern and elegant, high quality UI mockup, distinctive visual character",
    path="{workspace}/assets/design-reference-minimalist.png",
    image_size="landscape_16_9"
)

# 暗黑高端风参考图
GenerateImage(
    prompt="Dark mode luxury UI design, deep dark background (#1a1a2e), gold accents (#ffd700), premium feel, elegant typography, sophisticated card design, high-end brand style, professional UI mockup, distinctive visual character",
    path="{workspace}/assets/design-reference-dark-luxury.png",
    image_size="landscape_16_9"
)

# 清新自然风参考图
GenerateImage(
    prompt="Fresh natural UI design, green theme (#34c759), rounded corners, soft colors, lifestyle app interface, friendly and approachable, eco-friendly feel, modern mobile app mockup, distinctive visual character",
    path="{workspace}/assets/design-reference-fresh-natural.png",
    image_size="landscape_16_9"
)

# 社交活力风参考图
GenerateImage(
    prompt="Social media vibrant UI design, pink-purple gradient (#ff2d55), young and energetic, interactive elements, content cards, community app interface, trendy modern style, high quality mockup, distinctive visual character",
    path="{workspace}/assets/design-reference-social-vibrant.png",
    image_size="landscape_16_9"
)
```

#### 设计参考示例：

```
【现代电商风参考】
- 首页：顶部搜索框 + Banner轮播 + 金刚区入口 + 秒杀模块 + 商品瀑布流
- 商品卡片：圆角卡片、价格突出、标签醒目、hover动效
- 配色：主色#ff4757用于价格/按钮，背景#f5f5f5，卡片白色
- 字体：14px正文、16px标题、18px价格
- 圆角：12px卡片、8px按钮、9999px标签
```

**确认方式**：
1. 展示生成的参考图片
2. 使用 `AskUserQuestion` 让用户确认或调整
3. 如不满意，可重新生成或调整风格

---

### 步骤4️⃣：生成需求文档

**目的**：创建结构化的项目文档

**操作**：
- 使用 `references/requirements-template.md` 模板
- 生成：项目概述、功能需求、用户故事、非功能需求

**输出**：`需求文档.md`

---

### 步骤5️⃣：生成流程图

**目的**：可视化业务流程和交互逻辑

**操作**：
- 使用 Mermaid 语法
- 生成：系统架构图、业务流程图、交互流程图

**输出**：`流程图.md`

---

### 步骤6️⃣：生成Axure原型规范

**目的**：创建详细的原型设计规范

**操作**：使用 `references/axure-guide.md` 创建：
- 页面结构清单（文件夹组织）
- 交互说明文档
- 动态面板设计规范
- 组件库规范

**输出**：`Axure原型规范.md`

---

### 步骤7️⃣：生成页面跳转映射表

**目的**：定义完整的页面导航逻辑

**操作**：使用 `references/page-mapping-template.md` 创建：
- 页面清单（ID、名称、类型、优先级）
- 页面层级结构
- 跳转矩阵（60+条跳转规则）
- 参数规范和埋点规范

**输出**：`页面跳转映射表.md`

---

### 步骤8️⃣：生成HTML原型 ⭐⭐

**目的**：创建可运行的交互原型

**操作**：
```bash
python scripts/generate_project.py "项目名称" "./output" --style "现代电商风" --color "活力橙红"
```

**生成页面**：

| 文件 | 功能 | 交互 |
|------|------|------|
| index.html | 首页 | Banner轮播、分类入口、秒杀、推荐 |
| category.html | 分类页 | 侧边栏分类、子分类筛选 |
| product-detail.html | 商品详情 | 图片轮播、SKU选择、评价、收藏 |
| cart.html | 购物车 | 多店铺、地址选择、优惠券、结算 |
| user.html | 个人中心 | 用户信息、订单状态、功能菜单 |
| checkout.html | 订单确认 | 地址、商品清单、支付方式 |

**假数据内容**：
- 12+ 商品数据（含NEW/HOT标签、完整SKU）
- 2-3 购物车店铺
- 5 优惠券
- 3 收货地址
- 10 商品评价

**输出**：完整HTML原型目录

---

### 步骤9️⃣：生成设计稿

**目的**：创建高保真视觉设计

**操作**：使用 `GenerateImage` 生成：
- 线框图（Axure风格，标注交互）
- UI 设计稿（基于用户选择的风格）

**输出**：`assets/design-*.png`

---

## 🎨 设计风格配置详解

### 现代电商风（推荐）⭐

```css
:root {
    --primary: #ff4757;
    --primary-gradient: linear-gradient(135deg, #ff6b7a 0%, #ff4757 50%, #e84141 100%);
    --bg-page: #f5f5f5;
    --bg-card: #ffffff;
    --text-primary: #1a1a1a;
    --shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    --radius: 12px;
}
```

**特点**：
- 活力橙红色调，激发购买欲
- 精致卡片设计，层次分明
- 流畅动效，交互反馈及时
- 参考淘宝、京东等主流电商

**适用**：电商、零售、团购、促销活动页

---

### 简约扁平风

```css
:root {
    --primary: #667eea;
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --bg-page: #f8f9fc;
    --bg-card: #ffffff;
    --text-primary: #1a1a2e;
    --shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    --radius: 12px;
}
```

**特点**：
- 紫蓝渐变点缀
- 大量留白，视觉舒适
- 简洁线条，层次分明
- 圆角卡片设计

**适用**：工具类、企业应用、SaaS产品

---

### 暗黑高端风

```css
:root {
    --primary: #ffd700;
    --bg-page: #0f0f1a;
    --bg-card: #1a1a2e;
    --text-primary: #ffffff;
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    --radius: 16px;
}
```

**特点**：
- 深色背景，沉浸感强
- 金色点缀，高端品质
- 精致细节，层次丰富
- 毛玻璃效果

**适用**：奢侈品、会员应用、高端品牌

---

### 清新自然风

```css
:root {
    --primary: #34c759;
    --primary-gradient: linear-gradient(135deg, #38ef7d 0%, #11998e 100%);
    --bg-page: #f0fff4;
    --bg-card: #ffffff;
    --text-primary: #1a1a1a;
    --shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    --radius: 16px;
}
```

**特点**：
- 绿色系，自然清新
- 圆润设计，亲和力强
- 柔和配色，视觉舒适
- 大圆角卡片

**适用**：生活服务、健康应用、环保主题

---

### 社交活力风

```css
:root {
    --primary: #ff2d55;
    --primary-gradient: linear-gradient(135deg, #ff6b7a 0%, #ff2d55 100%);
    --bg-page: #fafafa;
    --bg-card: #ffffff;
    --text-primary: #1a1a1a;
    --shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    --radius: 12px;
}
```

**特点**：
- 粉红渐变，年轻活力
- 互动元素突出
- 内容卡片化展示
- 社交属性强

**适用**：社交应用、内容社区、短视频

---

## 🖌️ Frontend Design 原则

### 设计思维框架

编码前必须思考：

| 维度 | 问题 |
|------|------|
| **目的** | 这个界面解决什么问题？谁在使用？ |
| **风格基调** | 选择一个极端风格并坚持执行 |
| **约束** | 技术要求（框架、性能、无障碍） |
| **差异化** | 什么让这个界面**令人难忘**？ |

### 美学指南

#### 1. 排版 Typography
```
✅ 选择独特、有个性的字体
✅ 展示字体 + 正文字体搭配
❌ 避免：Inter、Roboto、Arial、系统字体
❌ 避免：Space Grotesk（AI常用）
```

#### 2. 配色 Color
```
✅ 使用CSS变量保持一致性
✅ 主导色 + 鲜明强调色
✅ 大胆的配色方案
❌ 避免：紫色渐变+白色背景（AI常用）
```

#### 3. 动效 Motion
```
✅ CSS优先（HTML项目）
✅ Motion库（React项目）
✅ 页面加载时的交错显示效果
✅ 高影响力的关键时刻
```

#### 4. 空间构图 Layout
```
✅ 意想不到的布局
✅ 不对称设计
✅ 元素重叠
✅ 对角线流动
✅ 打破网格
✅ 大量负空间 或 控制密度
```

#### 5. 背景与细节 Details
```
✅ 渐变网格
✅ 噪点纹理
✅ 几何图案
✅ 分层透明度
✅ 戏剧性阴影
✅ 装饰边框
✅ 自定义光标
✅ 颗粒叠加
```

### 反模式（避免）

| ❌ 避免 | 原因 |
|---------|------|
| Inter、Roboto、Arial | 过于常见，缺乏个性 |
| 紫色渐变+白色背景 | AI默认选择，千篇一律 |
| 可预测的布局 | 缺乏记忆点 |
| Space Grotesk | AI过度使用 |
| 模板化设计 | 缺乏上下文特色 |

---

## 📋 输出规范

### 文档输出

| 文件 | 格式 | 内容 |
|------|------|------|
| 需求文档.md | Markdown | 项目概述、功能需求、用户故事 |
| 流程图.md | Markdown + Mermaid | 系统架构、业务流程 |
| Axure原型规范.md | Markdown | 页面结构、交互说明 |
| 页面跳转映射表.md | Markdown | 页面清单、跳转矩阵 |

### HTML原型

| 文件 | 说明 | 完成度 |
|------|------|--------|
| index.html | 首页 | 100% |
| category.html | 分类页 | 100% |
| product-detail.html | 商品详情 | 100% |
| cart.html | 购物车 | 100% |
| user.html | 个人中心 | 100% |
| checkout.html | 订单确认 | 100% |
| styles.css | 样式 | 精美设计 |
| data.js | 假数据 | 丰富完整 |
| app.js | 交互脚本 | 完整功能 |

---

## 📁 输出文件结构

```
{项目名称}/
├── 📄 需求文档.md
├── 📊 流程图.md
├── 📋 Axure原型规范.md
├── 📑 页面跳转映射表.md
├── 📁 html/
│   ├── index.html
│   ├── category.html
│   ├── product-detail.html
│   ├── cart.html
│   ├── user.html
│   ├── checkout.html
│   ├── styles.css
│   ├── data.js
│   └── app.js
└── 📁 assets/
    ├── design-reference-*.png
    └── design-*.png
```

---

## ⚠️ 重要提示

1. **步骤确认**：每个关键步骤前使用 `AskUserQuestion` 确认
2. **风格一致**：HTML原型必须基于用户选择的设计风格
3. **完成度**：所有页面功能完整，交互可用
4. **美观度**：样式精美，符合现代设计规范
5. **设计参考**：生成前展示设计参考图片，让用户确认方向
6. **独特性**：避免AI默认风格，创造令人难忘的界面

---

## 🔄 版本历史

| 版本 | 更新内容 |
|------|---------|
| V9 Final | 整合frontend-design原则，完善设计参考图片生成 |
| V8 | 新增设计参考确认步骤，优化设计风格选项 |
| V7 | 添加设计风格确认步骤 |
| V6 | 完善所有页面功能和假数据 |
| V5 | 优化原型美观度 |
| V4 | 完善所有页面功能实现 |
