#!/usr/bin/env python3
"""
Project Builder V6 - 完整功能版
一键生成高完成度的项目原型，包含所有核心功能和交互

使用方法:
    python generate_project.py <项目名称> <输出目录>
"""

import os
import sys
import json
import random
import string
from datetime import datetime
from pathlib import Path

# ===========================
# 假数据生成
# ===========================

class FakeDataGenerator:
    """假数据生成器"""
    
    PRODUCT_NAMES = [
        "2024新款时尚休闲卫衣男", "纯棉宽松T恤女装", "复古刺绣连衣裙夏",
        "运动休闲鞋男透气", "真皮女士手提包", "智能运动手表心率监测",
        "无线蓝牙耳机降噪", "便携式移动电源20000毫安", "高清智能摄像头家用",
        "全自动滚筒洗衣机", "双门小型冰箱静音", "智能扫地机器人吸尘器"
    ]
    
    SHOP_NAMES = [
        "优品数码专营店", "时尚潮流服饰馆", "品质生活家居馆",
        "美妆护肤旗舰店", "运动户外专营店", "数码配件专营店"
    ]
    
    COUPONS = [
        {"name": "新人专享券", "amount": 20, "threshold": 99, "type": "新人", "valid": "2024-12-31"},
        {"name": "满减优惠券", "amount": 50, "threshold": 299, "type": "满减", "valid": "2024-12-31"},
        {"name": "店铺专用券", "amount": 10, "threshold": 59, "type": "店铺", "valid": "2024-12-31"},
        {"name": "限时秒杀券", "amount": 30, "threshold": 199, "type": "秒杀", "valid": "2024-12-31"},
        {"name": "生日特惠券", "amount": 100, "threshold": 499, "type": "生日", "valid": "2024-12-31"}
    ]
    
    CATEGORIES = [
        {"id": "clothing", "name": "服装", "icon": "👔", "sub": ["男装", "女装", "童装", "内衣"]},
        {"id": "shoes", "name": "鞋包", "icon": "👟", "sub": ["男鞋", "女鞋", "包包", "配饰"]},
        {"id": "digital", "name": "数码", "icon": "📱", "sub": ["手机", "电脑", "配件", "摄影"]},
        {"id": "home", "name": "家居", "icon": "🏠", "sub": ["家具", "家纺", "厨具", "灯具"]},
        {"id": "beauty", "name": "美妆", "icon": "💄", "sub": ["护肤", "彩妆", "香水", "工具"]},
        {"id": "food", "name": "食品", "icon": "🍔", "sub": ["零食", "生鲜", "饮料", "保健"]},
        {"id": "sports", "name": "运动", "icon": "⚽", "sub": ["运动服", "器材", "户外", "健身"]},
        {"id": "books", "name": "图书", "icon": "📚", "sub": ["文学", "教育", "科技", "艺术"]}
    ]
    
    COLORS = ["黑色", "白色", "红色", "蓝色", "灰色", "粉色", "绿色"]
    SIZES = ["XS", "S", "M", "L", "XL", "XXL"]
    CITIES = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "西安", "南京", "重庆"]
    DISTRICTS = ["朝阳区", "海淀区", "浦东新区", "天河区", "南山区", "西湖区", "武侯区", "雁塔区", "玄武区", "渝中区"]
    USER_NAMES = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"]
    
    REVIEW_CONTENTS = [
        "质量很好，包装也很精美，会回购的！",
        "物流很快，客服态度很好，满意！",
        "性价比很高，比实体店便宜多了，推荐购买！",
        "颜色和图片一致，没有色差，很满意！",
        "穿上去很舒服，尺码标准，下次还来！",
        "宝贝收到了，质量很好，价格实惠，值得购买！",
        "非常满意的一次购物体验，店家服务周到！",
        "东西不错，好评！",
        "比想象中还要好，真的太喜欢了！",
        "整体不错，就是快递有点慢"
    ]
    
    ORDERS = [
        {"status": "待付款", "icon": "💳", "count": 2},
        {"status": "待发货", "icon": "📦", "count": 1},
        {"status": "待收货", "icon": "🚚", "count": 3},
        {"status": "待评价", "icon": "⭐", "count": 5},
        {"status": "退款/售后", "icon": "🔧", "count": 0}
    ]
    
    @classmethod
    def generate_id(cls):
        return 'id_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    
    @classmethod
    def generate_products(cls, count=12):
        """生成商品列表"""
        products = []
        for i in range(count):
            original_price = random.randint(99, 999)
            discount = random.choice([0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
            current_price = int(original_price * discount)
            
            products.append({
                "id": cls.generate_id(),
                "name": cls.PRODUCT_NAMES[i % len(cls.PRODUCT_NAMES)],
                "image": f"https://picsum.photos/400/400?random={i+1}",
                "gallery": [f"https://picsum.photos/750/750?random={i*4+j}" for j in range(4)],
                "original_price": original_price,
                "current_price": current_price,
                "sold_count": random.randint(100, 10000),
                "good_rate": random.randint(90, 99),
                "colors": cls.COLORS[:random.randint(2, 5)],
                "sizes": cls.SIZES[:random.randint(3, 6)],
                "stock": random.randint(10, 500),
                "shop_name": cls.SHOP_NAMES[i % len(cls.SHOP_NAMES)],
                "shop_id": cls.generate_id(),
                "is_new": random.random() > 0.7,
                "is_hot": random.random() > 0.6,
                "tags": random.sample(["包邮", "极速退款", "七天无理由"], random.randint(1, 3))
            })
        return products
    
    @classmethod
    def generate_cart_data(cls):
        """生成购物车数据"""
        shops = []
        shop_count = random.randint(2, 3)
        
        for i in range(shop_count):
            products = []
            product_count = random.randint(1, 4)
            
            for j in range(product_count):
                original_price = random.randint(99, 999)
                discount = random.choice([0.8, 0.85, 0.9, 0.95])
                current_price = int(original_price * discount)
                
                product = {
                    "id": cls.generate_id(),
                    "name": cls.PRODUCT_NAMES[(i*3+j) % len(cls.PRODUCT_NAMES)],
                    "image": f"https://picsum.photos/400/400?random={i*10+j+10}",
                    "original_price": original_price,
                    "current_price": current_price,
                    "stock": random.randint(10, 500),
                    "quantity": random.randint(1, 3),
                    "selected": True,
                    "color": random.choice(cls.COLORS[:4]),
                    "size": random.choice(cls.SIZES[:4])
                }
                products.append(product)
            
            shops.append({
                "id": cls.generate_id(),
                "name": cls.SHOP_NAMES[i % len(cls.SHOP_NAMES)],
                "products": products
            })
        
        return shops
    
    @classmethod
    def generate_addresses(cls, count=3):
        """生成多个收货地址"""
        addresses = []
        for i in range(count):
            city = random.choice(cls.CITIES)
            addresses.append({
                "id": cls.generate_id(),
                "name": random.choice(cls.USER_NAMES),
                "phone": f"1{random.randint(3, 9)}{random.randint(100000000, 999999999)}",
                "province": city if city in ["北京", "上海"] else f"{city}省",
                "city": f"{city}市",
                "district": random.choice(cls.DISTRICTS),
                "address": f"{city}市{random.choice(cls.DISTRICTS)}某街道某号",
                "is_default": i == 0
            })
        return addresses
    
    @classmethod
    def generate_reviews(cls, count=10):
        """生成评价列表"""
        reviews = []
        for i in range(count):
            reviews.append({
                "id": cls.generate_id(),
                "user_name": f"用户{cls.generate_id()[:6]}",
                "avatar": f"https://api.dicebear.com/7.x/avataaars/svg?seed={cls.generate_id()}",
                "rating": random.randint(3, 5),
                "content": random.choice(cls.REVIEW_CONTENTS),
                "spec": f"{random.choice(cls.COLORS[:4])}/{random.choice(cls.SIZES[:4])}",
                "create_time": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "has_image": random.random() > 0.5,
                "images": [f"https://picsum.photos/200/200?random={i*3+j}" for j in range(random.randint(1, 3))] if random.random() > 0.5 else []
            })
        return reviews
    
    @classmethod
    def generate_user_info(cls):
        """生成用户信息"""
        return {
            "id": cls.generate_id(),
            "nickname": f"用户{random.randint(10000, 99999)}",
            "avatar": f"https://api.dicebear.com/7.x/avataaars/svg?seed={cls.generate_id()}",
            "phone": f"138****{random.randint(1000, 9999)}",
            "level": random.choice(["普通会员", "银卡会员", "金卡会员", "钻石会员"]),
            "points": random.randint(100, 5000),
            "coupons": random.randint(2, 10),
            "balance": round(random.uniform(0, 500), 2)
        }


# ===========================
# HTML 原型生成器
# ===========================

class HtmlPrototypeGenerator:
    """HTML 原型生成器"""
    
    def __init__(self, project_name, output_dir):
        self.project_name = project_name
        self.output_dir = Path(output_dir)
        self.data = FakeDataGenerator
        self.products = self.data.generate_products(12)
        self.cart_data = self.data.generate_cart_data()
        self.coupons = self.data.COUPONS
        self.addresses = self.data.generate_addresses(3)
        self.reviews = self.data.generate_reviews(10)
        self.user_info = self.data.generate_user_info()
        self.categories = self.data.CATEGORIES
        
    def generate(self):
        """生成完整的 HTML 原型"""
        sep = "=" * 50
        print(f"\n{sep}")
        print(f"Project Builder V6 - 完整功能版")
        print(f"{sep}\n")
        print(f"🚀 生成 HTML 原型: {self.project_name}\n")
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成 HTML 页面
        self.generate_index_page()
        self.generate_category_page()
        self.generate_product_detail_page()
        self.generate_cart_page()
        self.generate_user_page()
        self.generate_checkout_page()
        
        # 生成静态资源
        self.generate_css()
        self.generate_data_js()
        self.generate_app_js()
        
        print(f"\n✅ 原型生成完成!")
        print(f"📁 输出目录: {self.output_dir.resolve()}")
        print(f"🌐 打开 {self.output_dir / 'index.html'} 查看")
        print(f"\n{sep}")
        print(f"完成!")
        print(f"{sep}\n")
    
    def generate_index_page(self):
        """生成首页"""
        html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>首页 - ''' + self.project_name + '''</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- 顶部导航栏 -->
    <header class="header" id="header">
        <div class="container header-content">
            <div class="logo">🏪 ''' + self.project_name + '''</div>
            <div class="search-box">
                <input type="text" placeholder="搜索商品、品牌..." id="searchInput" onkeyup="handleSearch(event)">
                <button onclick="search()">🔍</button>
                <div class="search-suggestions" id="searchSuggestions"></div>
            </div>
            <div class="header-actions">
                <span class="cart-icon" onclick="goToCart()">
                    🛒 
                    <span class="badge" id="cartBadge">''' + str(sum(len(s['products']) for s in self.cart_data)) + '''</span>
                </span>
                <span class="user-icon" onclick="goToUser()">👤</span>
            </div>
        </div>
    </header>

    <!-- 主导航 -->
    <nav class="main-nav">
        <div class="container">
            <ul class="nav-list">
                <li class="active"><a href="index.html">首页</a></li>
                <li><a href="category.html">全部分类</a></li>
                <li><a href="#products">商品列表</a></li>
                <li><a href="cart.html">购物车</a></li>
                <li><a href="user.html">我的</a></li>
            </ul>
        </div>
    </nav>

    <!-- Banner 轮播 -->
    <section class="banner">
        <div class="banner-slider" id="bannerSlider">
            <div class="banner-item" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);" onclick="goToPromotion('new')">
                <div class="banner-content">
                    <span class="banner-tag">新品上市</span>
                    <h2>🎉 限时优惠 全场满减</h2>
                    <p>满199减50 / 满299减100</p>
                    <button class="banner-btn">立即抢购 →</button>
                </div>
            </div>
            <div class="banner-item" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);" onclick="goToPromotion('hot')">
                <div class="banner-content">
                    <span class="banner-tag">爆款推荐</span>
                    <h2>🔥 品质好物 低至5折</h2>
                    <p>精选爆款 限时特惠</p>
                    <button class="banner-btn">去逛逛 →</button>
                </div>
            </div>
            <div class="banner-item" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);" onclick="goToPromotion('vip')">
                <div class="banner-content">
                    <span class="banner-tag">会员专享</span>
                    <h2>✨ 加入会员 享专属折扣</h2>
                    <p>每月专属优惠券礼包</p>
                    <button class="banner-btn">立即加入 →</button>
                </div>
            </div>
        </div>
        <div class="banner-indicators">
            <span class="active" onclick="goToSlide(0)"></span>
            <span onclick="goToSlide(1)"></span>
            <span onclick="goToSlide(2)"></span>
        </div>
    </section>

    <!-- 快捷入口 -->
    <section class="quick-entry">
        <div class="container">
            <div class="quick-grid">
                ''' + self._generate_category_grid() + '''
            </div>
        </div>
    </section>

    <!-- 限时秒杀 -->
    <section class="seckill">
        <div class="container">
            <div class="section-header">
                <div class="section-title">
                    <h2>⚡ 限时秒杀</h2>
                    <span class="section-subtitle">每日好价 限量抢购</span>
                </div>
                <div class="countdown">
                    <span class="countdown-label">距离结束</span>
                    <span class="time" id="hours">02</span>
                    <span class="time-sep">:</span>
                    <span class="time" id="minutes">45</span>
                    <span class="time-sep">:</span>
                    <span class="time" id="seconds">30</span>
                </div>
            </div>
            <div class="seckill-list">
                ''' + self._generate_seckill_items() + '''
            </div>
        </div>
    </section>

    <!-- 推荐商品 -->
    <section class="recommend-section" id="products">
        <div class="container">
            <div class="section-header">
                <div class="section-title">
                    <h3>🔥 为你推荐</h3>
                    <span class="section-subtitle">精选好物 品质保证</span>
                </div>
                <div class="filter-tabs">
                    <span class="tab active" onclick="filterProducts('all', this)">全部</span>
                    <span class="tab" onclick="filterProducts('new', this)">新品</span>
                    <span class="tab" onclick="filterProducts('hot', this)">热卖</span>
                    <span class="tab" onclick="filterProducts('sale', this)">特惠</span>
                </div>
            </div>
            <div class="product-grid" id="productGrid">
                ''' + self._generate_product_grid() + '''
            </div>
            <div class="load-more">
                <button class="btn-load-more" onclick="loadMoreProducts()">
                    <span>加载更多</span>
                    <span class="loading-spinner" style="display:none;">⏳</span>
                </button>
            </div>
        </div>
    </section>

    <!-- 底部导航 -->
    <nav class="bottom-nav">
        <a href="index.html" class="nav-item active">
            <span class="nav-icon">🏠</span>
            <span>首页</span>
        </a>
        <a href="category.html" class="nav-item">
            <span class="nav-icon">📑</span>
            <span>分类</span>
        </a>
        <a href="cart.html" class="nav-item">
            <span class="nav-icon">🛒</span>
            <span>购物车</span>
        </a>
        <a href="user.html" class="nav-item">
            <span class="nav-icon">👤</span>
            <span>我的</span>
        </a>
    </nav>

    <!-- Toast提示 -->
    <div class="toast" id="toast"></div>

    <script src="data.js"></script>
    <script src="app.js"></script>
</body>
</html>'''
        
        (self.output_dir / 'index.html').write_text(html, encoding='utf-8')
        print("✅ 生成: index.html")
    
    def _generate_category_grid(self):
        """生成分类网格"""
        items = []
        for cat in self.categories:
            items.append(f'''
                <div class="quick-item" onclick="goToCategory('{cat['id']}')">
                    <div class="quick-icon">{cat['icon']}</div>
                    <span>{cat['name']}</span>
                </div>''')
        return ''.join(items)
    
    def _generate_seckill_items(self):
        """生成秒杀商品"""
        items = []
        for i, p in enumerate(self.products[:4]):
            progress = random.randint(30, 95)
            items.append(f'''
                <div class="seckill-item" onclick="goToProduct('{p['id']}')">
                    <div class="seckill-img-wrapper">
                        <img src="{p['image']}" alt="{p['name']}">
                        <span class="seckill-tag">-{int((1-0.7)*100)}%</span>
                    </div>
                    <div class="seckill-info">
                        <div class="seckill-price-row">
                            <span class="seckill-price">¥{int(p['current_price'] * 0.7)}</span>
                            <span class="seckill-original">¥{p['current_price']}</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress" style="width: {progress}%"></div>
                        </div>
                        <div class="seckill-sold">已抢{progress}%</div>
                    </div>
                </div>''')
        return ''.join(items)
    
    def _generate_product_grid(self):
        """生成商品网格"""
        cards = []
        for p in self.products:
            tags_html = ''.join([f'<span class="product-tag">{t}</span>' for t in p['tags'][:2]])
            new_badge = '<span class="product-badge new">NEW</span>' if p['is_new'] else ''
            hot_badge = '<span class="product-badge hot">HOT</span>' if p['is_hot'] else ''
            
            cards.append(f'''
                <div class="product-card" onclick="goToProduct('{p['id']}')" data-category="{'new' if p['is_new'] else 'hot' if p['is_hot'] else 'all'}">
                    <div class="product-img-wrapper">
                        <img src="{p['image']}" alt="{p['name']}" class="product-img">
                        {new_badge}
                        {hot_badge}
                    </div>
                    <div class="product-info">
                        <div class="product-tags">{tags_html}</div>
                        <div class="product-title">{p['name']}</div>
                        <div class="product-price-row">
                            <span class="current-price">¥{p['current_price']}</span>
                            <span class="original-price">¥{p['original_price']}</span>
                        </div>
                        <div class="product-meta">
                            <span class="sold">已售{p['sold_count']}+</span>
                            <span class="rate">好评{p['good_rate']}%</span>
                        </div>
                    </div>
                </div>''')
        return ''.join(cards)
    
    def generate_category_page(self):
        """生成分类页"""
        categories_html = ''
        for cat in self.categories:
            sub_cats = ''.join([f'<span class="sub-cat" onclick="filterBySubCat(\'{sub}\')">{sub}</span>' for sub in cat['sub']])
            categories_html += f'''
                <div class="category-item" onclick="selectCategory('{cat['id']}')">
                    <div class="cat-icon">{cat['icon']}</div>
                    <div class="cat-info">
                        <span class="cat-name">{cat['name']}</span>
                        <div class="cat-subs">{sub_cats}</div>
                    </div>
                    <span class="cat-arrow">→</span>
                </div>'''
        
        html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>商品分类 - ''' + self.project_name + '''</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="category-page">
    <!-- 顶部导航栏 -->
    <header class="header">
        <div class="container header-content">
            <a href="javascript:history.back()" class="back-btn">←</a>
            <div class="search-box" style="flex:1;max-width:none;margin:0 15px;">
                <input type="text" placeholder="搜索商品..." id="searchInput">
                <button onclick="search()">🔍</button>
            </div>
            <span onclick="showFilter()">筛选</span>
        </div>
    </header>

    <!-- 分类内容 -->
    <div class="category-content">
        <div class="category-sidebar">
            ''' + ''.join([f'<div class="sidebar-item {"active" if i==0 else ""}" onclick="selectSidebarCat({i}, this)">{cat["name"]}</div>' for i, cat in enumerate(self.categories)]) + '''
        </div>
        <div class="category-main">
            <div class="category-banner">
                <img src="https://picsum.photos/600/200?random=100" alt="分类banner">
            </div>
            <div class="category-list">
                ''' + categories_html + '''
            </div>
        </div>
    </div>

    <!-- 底部导航 -->
    <nav class="bottom-nav">
        <a href="index.html" class="nav-item">
            <span class="nav-icon">🏠</span>
            <span>首页</span>
        </a>
        <a href="category.html" class="nav-item active">
            <span class="nav-icon">📑</span>
            <span>分类</span>
        </a>
        <a href="cart.html" class="nav-item">
            <span class="nav-icon">🛒</span>
            <span>购物车</span>
        </a>
        <a href="user.html" class="nav-item">
            <span class="nav-icon">👤</span>
            <span>我的</span>
        </a>
    </nav>

    <script src="data.js"></script>
    <script src="app.js"></script>
</body>
</html>'''
        
        (self.output_dir / 'category.html').write_text(html, encoding='utf-8')
        print("✅ 生成: category.html")
    
    def generate_product_detail_page(self):
        """生成商品详情页"""
        product = self.products[0]
        
        gallery_items = ''.join([f'<div class="gallery-item" style="background-image: url(\'{img}\')"></div>' for img in product['gallery']])
        gallery_indicators = ''.join(['<span class="active"></span>' if i == 0 else '<span></span>' for i in range(len(product['gallery']))])
        
        reviews_html = ''
        for r in self.reviews[:3]:
            stars = '⭐' * r['rating']
            images_html = ''.join([f'<img src="{img}" class="review-img">' for img in r['images'][:3]]) if r['images'] else ''
            reviews_html += f'''
                <div class="review-item">
                    <div class="review-header">
                        <img src="{r['avatar']}" alt="" class="review-avatar">
                        <div class="review-user-info">
                            <span class="review-user">{r['user_name']}</span>
                            <span class="review-rating">{stars}</span>
                        </div>
                        <span class="review-date">{r['create_time']}</span>
                    </div>
                    <div class="review-content">{r['content']}</div>
                    <div class="review-images">{images_html}</div>
                    <div class="review-meta">
                        <span class="review-spec">购买规格: {r['spec']}</span>
                    </div>
                </div>'''
        
        colors_html = ''.join([f'<span class="sku-value {"active" if i==0 else ""}" onclick="selectSku(\'color\', \'{c}\', this)">{c}</span>' for i, c in enumerate(product['colors'])])
        sizes_html = ''.join([f'<span class="sku-value {"active" if i==0 else ""}" onclick="selectSku(\'size\', \'{s}\', this)">{s}</span>' for i, s in enumerate(product['sizes'])])
        
        coupons_html = ''.join([f'''
            <div class="coupon-item">
                <div class="coupon-left">
                    <div class="coupon-amount">¥{c['amount']}</div>
                    <div class="coupon-threshold">满{c['threshold']}可用</div>
                </div>
                <div class="coupon-right">
                    <div class="coupon-name">{c['name']}</div>
                    <div class="coupon-valid">有效期至{c['valid']}</div>
                    <button class="coupon-btn" onclick="claimCoupon(this, {c['amount']})">领取</button>
                </div>
            </div>''' for c in self.coupons])
        
        similar_html = ''.join([f'''
            <div class="product-card" onclick="goToProduct('{p['id']}')">
                <img src="{p['image']}" alt="{p['name']}" class="product-img">
                <div class="product-info">
                    <div class="product-title">{p['name']}</div>
                    <div class="product-price-row">
                        <span class="current-price">¥{p['current_price']}</span>
                    </div>
                </div>
            </div>''' for p in self.products[1:5]])
        
        html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + product['name'] + ''' - ''' + self.project_name + '''</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="product-detail-page">
    <!-- 顶部导航栏 -->
    <header class="header header-fixed" id="detailHeader">
        <div class="container header-content">
            <a href="javascript:history.back()" class="back-btn">←</a>
            <div class="header-tabs" id="headerTabs">
                <span class="tab active" onclick="scrollToSection('product')">商品</span>
                <span class="tab" onclick="scrollToSection('detail')">详情</span>
                <span class="tab" onclick="scrollToSection('reviews')">评价</span>
            </div>
            <div class="header-actions">
                <span onclick="shareProduct()">📤</span>
                <span onclick="showMoreMenu()">⋮</span>
            </div>
        </div>
    </header>

    <!-- 商品轮播图 -->
    <section class="product-gallery" id="product">
        <div class="gallery-slider" id="gallerySlider">
            ''' + gallery_items + '''
        </div>
        <div class="gallery-indicators">
            ''' + gallery_indicators + '''
        </div>
        <div class="gallery-counter">
            <span id="currentSlide">1</span> / ''' + str(len(product['gallery'])) + '''
        </div>
    </section>

    <!-- 商品信息 -->
    <section class="product-info-section">
        <div class="container">
            <div class="product-price-row">
                <div class="price-main">
                    <span class="price-symbol">¥</span>
                    <span class="current-price">''' + str(product['current_price']) + '''</span>
                    <span class="original-price">¥''' + str(product['original_price']) + '''</span>
                </div>
                <span class="discount-tag">限时特惠</span>
            </div>
            <h1 class="product-title">''' + product['name'] + '''</h1>
            <div class="product-tags-row">
                <span class="tag">🔥 月销''' + str(product['sold_count']) + '''+</span>
                <span class="tag">⭐ 好评''' + str(product['good_rate']) + '''%</span>
                <span class="tag">📦 极速发货</span>
            </div>
        </div>
    </section>

    <!-- 促销信息 -->
    <section class="promotion-section" onclick="showCouponModal()">
        <div class="container">
            <div class="promotion-row">
                <span class="label">优惠</span>
                <div class="promotion-tags">
                    <span class="promotion-tag">满199减20</span>
                    <span class="promotion-tag">满299减50</span>
                </div>
                <span class="arrow">领券 ></span>
            </div>
        </div>
    </section>

    <!-- 规格选择 -->
    <section class="sku-section" onclick="showSkuModal()">
        <div class="container">
            <div class="sku-row">
                <span class="label">已选</span>
                <span class="value" id="selectedSkuText">''' + product['colors'][0] + ''' / ''' + product['sizes'][0] + '''，1件</span>
                <span class="arrow">></span>
            </div>
        </div>
    </section>

    <!-- 店铺信息 -->
    <section class="shop-section">
        <div class="container">
            <div class="shop-info">
                <img src="https://picsum.photos/100/100?random=50" class="shop-logo">
                <div class="shop-detail">
                    <div class="shop-name">''' + product['shop_name'] + '''</div>
                    <div class="shop-meta">
                        <span>商品 4.9</span>
                        <span>物流 4.8</span>
                        <span>服务 4.9</span>
                    </div>
                </div>
                <button class="btn-enter-shop" onclick="goToShop(''' + product['shop_id'] + ''')">进店 ></button>
            </div>
        </div>
    </section>

    <!-- 商品评价 -->
    <section class="reviews-section" id="reviews">
        <div class="container">
            <div class="reviews-header">
                <div class="reviews-title">
                    <h3>商品评价</h3>
                    <span class="reviews-count">(''' + str(len(self.reviews)) + ''')</span>
                </div>
                <span class="good-rate">好评率 ''' + str(product['good_rate']) + '''% ></span>
            </div>
            <div class="review-tags">
                <span class="tag active" onclick="filterReviews('all', this)">全部</span>
                <span class="tag" onclick="filterReviews('image', this)">有图(''' + str(sum(1 for r in self.reviews if r['has_image'])) + ''')</span>
                <span class="tag" onclick="filterReviews('good', this)">好评(''' + str(sum(1 for r in self.reviews if r['rating'] >= 4)) + ''')</span>
                <span class="tag" onclick="filterReviews('medium', this)">中评(''' + str(sum(1 for r in self.reviews if r['rating'] == 3)) + ''')</span>
                <span class="tag" onclick="filterReviews('bad', this)">差评(''' + str(sum(1 for r in self.reviews if r['rating'] < 3)) + ''')</span>
            </div>
            <div class="review-list" id="reviewList">
                ''' + reviews_html + '''
            </div>
            <button class="btn-more-reviews" onclick="goToAllReviews()">查看全部评价</button>
        </div>
    </section>

    <!-- 商品详情 -->
    <section class="product-detail-content" id="detail">
        <div class="container">
            <div class="detail-tabs">
                <span class="tab active">图文详情</span>
                <span class="tab">规格参数</span>
                <span class="tab">售后保障</span>
            </div>
            <div class="detail-images">
                <img src="https://picsum.photos/750/400?random=30" alt="详情图1">
                <img src="https://picsum.photos/750/400?random=31" alt="详情图2">
                <img src="https://picsum.photos/750/400?random=32" alt="详情图3">
                <img src="https://picsum.photos/750/400?random=33" alt="详情图4">
            </div>
        </div>
    </section>

    <!-- 相似推荐 -->
    <section class="similar-section">
        <div class="container">
            <div class="section-header">
                <h3>🔥 相似推荐</h3>
            </div>
            <div class="product-grid">
                ''' + similar_html + '''
            </div>
        </div>
    </section>

    <!-- 底部操作栏 -->
    <section class="bottom-actions-bar">
        <div class="action-icons">
            <div class="action-item" onclick="contactService()">
                <span>💬</span>
                <span>客服</span>
            </div>
            <div class="action-item" onclick="goToShop(''' + product['shop_id'] + ''')">
                <span>🏪</span>
                <span>店铺</span>
            </div>
            <div class="action-item" id="favoriteBtn" onclick="toggleFavorite()">
                <span id="favoriteIcon">⭐</span>
                <span id="favoriteText">收藏</span>
            </div>
        </div>
        <div class="action-buttons">
            <button class="btn-add-cart" onclick="addToCart()">
                <span class="btn-price">¥''' + str(product['current_price']) + '''</span>
                <span class="btn-text">加入购物车</span>
            </button>
            <button class="btn-buy-now" onclick="buyNow()">
                <span class="btn-price">¥''' + str(product['current_price']) + '''</span>
                <span class="btn-text">立即购买</span>
            </button>
        </div>
    </section>

    <!-- SKU 选择弹窗 -->
    <div class="modal" id="skuModal">
        <div class="modal-mask" onclick="closeSkuModal()"></div>
        <div class="modal-content sku-modal">
            <div class="sku-header">
                <img src="''' + product['image'] + '''" alt="" class="sku-product-img">
                <div class="sku-info">
                    <div class="sku-price-row">
                        <span class="sku-price">¥''' + str(product['current_price']) + '''</span>
                        <span class="sku-stock">库存 ''' + str(product['stock']) + ''' 件</span>
                    </div>
                    <div class="sku-selected" id="skuSelected">已选: ''' + product['colors'][0] + '''、''' + product['sizes'][0] + '''</div>
                </div>
                <span class="sku-close" onclick="closeSkuModal()">✕</span>
            </div>
            <div class="sku-body">
                <div class="sku-option">
                    <div class="sku-option-title">颜色</div>
                    <div class="sku-option-values">
                        ''' + colors_html + '''
                    </div>
                </div>
                <div class="sku-option">
                    <div class="sku-option-title">尺码</div>
                    <div class="sku-option-values">
                        ''' + sizes_html + '''
                    </div>
                </div>
                <div class="quantity-selector">
                    <span class="label">购买数量</span>
                    <div class="quantity-control">
                        <button class="qty-btn" onclick="decreaseQty()">-</button>
                        <input type="number" id="quantityInput" value="1" min="1" max="''' + str(product['stock']) + '''">
                        <button class="qty-btn" onclick="increaseQty()">+</button>
                    </div>
                </div>
            </div>
            <div class="sku-footer">
                <button class="btn-confirm-sku" onclick="confirmSku()">确定</button>
            </div>
        </div>
    </div>

    <!-- 优惠券弹窗 -->
    <div class="modal" id="couponModal">
        <div class="modal-mask" onclick="closeCouponModal()"></div>
        <div class="modal-content coupon-modal">
            <div class="modal-header">
                <h3>领取优惠券</h3>
                <span class="modal-close" onclick="closeCouponModal()">✕</span>
            </div>
            <div class="coupon-list">
                ''' + coupons_html + '''
            </div>
        </div>
    </div>

    <!-- Toast提示 -->
    <div class="toast" id="toast"></div>

    <script src="data.js"></script>
    <script src="app.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            initProductDetailPage();
        });
    </script>
</body>
</html>'''
        
        (self.output_dir / 'product-detail.html').write_text(html, encoding='utf-8')
        print("✅ 生成: product-detail.html")
    
    def generate_cart_page(self):
        """生成购物车页"""
        total_items = sum(len(s['products']) for s in self.cart_data)
        
        shops_html = ''
        for shop in self.cart_data:
            products_html = ''
            for p in shop['products']:
                products_html += f'''
                <div class="cart-item" data-id="{p['id']}">
                    <input type="checkbox" class="item-checkbox" checked data-price="{p['current_price']}" data-qty="{p['quantity']}">
                    <img src="{p['image']}" class="cart-item-img" onclick="goToProduct('{p['id']}')">
                    <div class="cart-item-info">
                        <div class="cart-item-title" onclick="goToProduct('{p['id']}')">{p['name']}</div>
                        <div class="cart-item-spec" onclick="showSkuModal()">{p['color']} / {p['size']} ></div>
                        <div class="cart-item-bottom">
                            <span class="cart-item-price">¥{p['current_price']}</span>
                            <div class="cart-item-actions">
                                <button class="qty-btn" onclick="changeQty(this, -1)">-</button>
                                <input type="number" value="{p['quantity']}" min="1" max="{p['stock']}" class="qty-input" onchange="updateCartTotal()">
                                <button class="qty-btn" onclick="changeQty(this, 1)">+</button>
                            </div>
                        </div>
                    </div>
                </div>'''
            
            shops_html += f'''
            <div class="cart-shop" data-shop-id="{shop['id']}">
                <div class="cart-shop-header">
                    <input type="checkbox" class="shop-checkbox" checked onchange="toggleShopItems(this)">
                    <span class="cart-shop-name" onclick="goToShop('{shop['id']}')">🏪 {shop['name']}</span>
                    <span class="cart-shop-coupon" onclick="showCartCouponModal('{shop['id']}')">领券 ></span>
                </div>
                <div class="cart-shop-products">
                    {products_html}
                </div>
            </div>'''
        
        recommendations_html = ''.join([f'''
            <div class="product-card" onclick="goToProduct('{p['id']}')">
                <img src="{p['image']}" alt="{p['name']}" class="product-img">
                <div class="product-info">
                    <div class="product-title">{p['name']}</div>
                    <div class="product-price-row">
                        <span class="current-price">¥{p['current_price']}</span>
                    </div>
                    <div class="product-meta">已售{p['sold_count']}+</div>
                </div>
            </div>''' for p in self.products[4:8]])
        
        html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>购物车 - ''' + self.project_name + '''</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="cart-page">
    <!-- 顶部导航栏 -->
    <header class="header">
        <div class="container header-content">
            <h1>购物车 (''' + str(total_items) + ''')</h1>
            <span class="edit-btn" id="editBtn" onclick="toggleEditMode()">管理</span>
        </div>
    </header>

    <!-- 收货地址 -->
    <section class="address-section" onclick="showAddressModal()">
        <div class="container">
            <div class="address-card">
                <div class="address-icon">📍</div>
                <div class="address-info">
                    <div class="address-header">
                        <span class="name">''' + self.addresses[0]['name'] + '''</span>
                        <span class="phone">''' + self.addresses[0]['phone'] + '''</span>
                        <span class="default-tag">默认</span>
                    </div>
                    <div class="address-detail">''' + self.addresses[0]['province'] + self.addresses[0]['city'] + self.addresses[0]['district'] + self.addresses[0]['address'] + '''</div>
                </div>
                <div class="address-arrow">></div>
            </div>
        </div>
    </section>

    <!-- 购物车内容 -->
    <main class="cart-content">
        <div class="container">
            ''' + shops_html + '''
        </div>
        
        <!-- 空状态 -->
        <div class="empty-cart" id="emptyCart" style="display:none;">
            <div class="empty-icon">🛒</div>
            <div class="empty-text">购物车是空的</div>
            <button class="btn-go-shopping" onclick="goToIndex()">去逛逛</button>
        </div>
        
        <!-- 为你推荐 -->
        <section class="recommend-section">
            <div class="container">
                <div class="section-header">
                    <h3>💡 为你推荐</h3>
                </div>
                <div class="product-grid">
                    ''' + recommendations_html + '''
                </div>
            </div>
        </section>
    </main>

    <!-- 底部结算栏 -->
    <div class="cart-footer">
        <div class="container">
            <div class="footer-left">
                <label class="select-all" onclick="toggleSelectAll()">
                    <input type="checkbox" id="selectAll" checked>
                    <span>全选</span>
                </label>
            </div>
            <div class="footer-right" id="settleSection">
                <div class="total-info">
                    <div class="total-row">
                        <span>合计:</span>
                        <span class="total-price" id="totalPrice">¥0.00</span>
                    </div>
                    <div class="discount-info" id="discountInfo">已优惠 ¥0.00</div>
                </div>
                <button class="btn-settle" id="btnSettle" onclick="goCheckout()">结算(0)</button>
            </div>
            <div class="footer-right delete-section" id="deleteSection" style="display:none;">
                <button class="btn-fav" onclick="moveToFavorite()">移入收藏</button>
                <button class="btn-delete" onclick="deleteSelected()">删除</button>
            </div>
        </div>
    </div>

    <!-- 地址选择弹窗 -->
    <div class="modal" id="addressModal">
        <div class="modal-mask" onclick="closeAddressModal()"></div>
        <div class="modal-content address-modal">
            <div class="modal-header">
                <h3>选择收货地址</h3>
                <span class="modal-close" onclick="closeAddressModal()">✕</span>
            </div>
            <div class="address-list">
                ''' + ''.join([f'''
                <div class="address-item {"active" if addr['is_default'] else ""}" onclick="selectAddress('{addr['id']}')">
                    <div class="address-select">{'✓' if addr['is_default'] else ''}</div>
                    <div class="address-content">
                        <div class="address-user">
                            <span class="name">{addr['name']}</span>
                            <span class="phone">{addr['phone']}</span>
                            {'' if not addr['is_default'] else '<span class="default-badge">默认</span>'}
                        </div>
                        <div class="address-full">{addr['province']}{addr['city']}{addr['district']}{addr['address']}</div>
                    </div>
                </div>''' for addr in self.addresses]) + '''
            </div>
            <button class="btn-add-address" onclick="addNewAddress()">+ 添加新地址</button>
        </div>
    </div>

    <!-- 优惠券选择弹窗 -->
    <div class="modal" id="cartCouponModal">
        <div class="modal-mask" onclick="closeCartCouponModal()"></div>
        <div class="modal-content coupon-modal">
            <div class="modal-header">
                <h3>选择优惠券</h3>
                <span class="modal-close" onclick="closeCartCouponModal()">✕</span>
            </div>
            <div class="coupon-list">
                ''' + ''.join([f'''
                <div class="coupon-item selectable" onclick="selectCartCoupon(this, {c['amount']})">
                    <div class="coupon-left">
                        <div class="coupon-amount">¥{c['amount']}</div>
                        <div class="coupon-threshold">满{c['threshold']}可用</div>
                    </div>
                    <div class="coupon-right">
                        <div class="coupon-name">{c['name']}</div>
                        <div class="coupon-valid">有效期至{c['valid']}</div>
                    </div>
                    <div class="coupon-select">○</div>
                </div>''' for c in self.coupons[:3]]) + '''
            </div>
        </div>
    </div>

    <!-- Toast提示 -->
    <div class="toast" id="toast"></div>

    <script src="data.js"></script>
    <script src="app.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            initCartPage();
        });
    </script>
</body>
</html>'''
        
        (self.output_dir / 'cart.html').write_text(html, encoding='utf-8')
        print("✅ 生成: cart.html")
    
    def generate_user_page(self):
        """生成用户中心页"""
        orders_html = ''.join([f'''
            <div class="order-item" onclick="goToOrders('{o['status']}' )">
                <span class="order-icon">{o['icon']}</span>
                <span class="order-name">{o['status']}</span>
                {'<span class="order-badge">' + str(o['count']) + '</span>' if o['count'] > 0 else ''}
            </div>''' for o in self.data.ORDERS])
        
        html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的 - ''' + self.project_name + '''</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="user-page">
    <!-- 顶部导航栏 -->
    <header class="header">
        <div class="container header-content">
            <span>设置</span>
            <h1>个人中心</h1>
            <span onclick="showMessage()">消息</span>
        </div>
    </header>

    <!-- 用户信息 -->
    <section class="user-info-section">
        <div class="container">
            <div class="user-profile">
                <img src="''' + self.user_info['avatar'] + '''" alt="头像" class="user-avatar">
                <div class="user-detail">
                    <div class="user-name">''' + self.user_info['nickname'] + '''</div>
                    <div class="user-level">''' + self.user_info['level'] + '''</div>
                    <div class="user-id">ID: ''' + self.user_info['id'] + '''</div>
                </div>
                <button class="btn-edit-profile" onclick="editProfile()">编辑资料 ></button>
            </div>
            <div class="user-stats">
                <div class="stat-item" onclick="goToCollection()">
                    <span class="stat-value">12</span>
                    <span class="stat-label">收藏</span>
                </div>
                <div class="stat-item" onclick="goToHistory()">
                    <span class="stat-value">28</span>
                    <span class="stat-label">足迹</span>
                </div>
                <div class="stat-item" onclick="goToCoupons()">
                    <span class="stat-value">''' + str(self.user_info['coupons']) + '''</span>
                    <span class="stat-label">优惠券</span>
                </div>
                <div class="stat-item" onclick="goToPoints()">
                    <span class="stat-value">''' + str(self.user_info['points']) + '''</span>
                    <span class="stat-label">积分</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 我的订单 -->
    <section class="orders-section">
        <div class="container">
            <div class="section-title-row">
                <h3>我的订单</h3>
                <span class="view-all" onclick="goToOrders('all')">查看全部 ></span>
            </div>
            <div class="orders-grid">
                ''' + orders_html + '''
            </div>
        </div>
    </section>

    <!-- 功能菜单 -->
    <section class="menu-section">
        <div class="container">
            <div class="menu-group">
                <div class="menu-item" onclick="goToAddress()">
                    <span class="menu-icon">📍</span>
                    <span class="menu-text">收货地址</span>
                    <span class="menu-arrow">></span>
                </div>
                <div class="menu-item" onclick="goToService()">
                    <span class="menu-icon">💬</span>
                    <span class="menu-text">客服中心</span>
                    <span class="menu-arrow">></span>
                </div>
                <div class="menu-item" onclick="goToHelp()">
                    <span class="menu-icon">❓</span>
                    <span class="menu-text">帮助中心</span>
                    <span class="menu-arrow">></span>
                </div>
            </div>
            <div class="menu-group">
                <div class="menu-item" onclick="goToSettings()">
                    <span class="menu-icon">⚙️</span>
                    <span class="menu-text">设置</span>
                    <span class="menu-arrow">></span>
                </div>
                <div class="menu-item" onclick="goToAbout()">
                    <span class="menu-icon">ℹ️</span>
                    <span class="menu-text">关于我们</span>
                    <span class="menu-arrow">></span>
                </div>
            </div>
        </div>
    </section>

    <!-- 底部导航 -->
    <nav class="bottom-nav">
        <a href="index.html" class="nav-item">
            <span class="nav-icon">🏠</span>
            <span>首页</span>
        </a>
        <a href="category.html" class="nav-item">
            <span class="nav-icon">📑</span>
            <span>分类</span>
        </a>
        <a href="cart.html" class="nav-item">
            <span class="nav-icon">🛒</span>
            <span>购物车</span>
        </a>
        <a href="user.html" class="nav-item active">
            <span class="nav-icon">👤</span>
            <span>我的</span>
        </a>
    </nav>

    <script src="data.js"></script>
    <script src="app.js"></script>
</body>
</html>'''
        
        (self.output_dir / 'user.html').write_text(html, encoding='utf-8')
        print("✅ 生成: user.html")
    
    def generate_checkout_page(self):
        """生成订单确认页"""
        html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>确认订单 - ''' + self.project_name + '''</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="checkout-page">
    <!-- 顶部导航栏 -->
    <header class="header">
        <div class="container header-content">
            <a href="javascript:history.back()" class="back-btn">←</a>
            <h1>确认订单</h1>
            <span></span>
        </div>
    </header>

    <!-- 地址选择 -->
    <section class="address-section" onclick="showAddressModal()">
        <div class="container">
            <div class="address-card">
                <div class="address-icon">📍</div>
                <div class="address-info">
                    <div class="address-header">
                        <span class="name">''' + self.addresses[0]['name'] + '''</span>
                        <span class="phone">''' + self.addresses[0]['phone'] + '''</span>
                    </div>
                    <div class="address-detail">''' + self.addresses[0]['province'] + self.addresses[0]['city'] + self.addresses[0]['district'] + self.addresses[0]['address'] + '''</div>
                </div>
                <div class="address-arrow">></div>
            </div>
        </div>
    </section>

    <!-- 商品清单 -->
    <section class="checkout-goods">
        <div class="container">
            <div class="shop-name">🏪 优品数码专营店</div>
            <div class="checkout-item">
                <img src="''' + self.products[0]['image'] + '''" class="item-img">
                <div class="item-info">
                    <div class="item-title">''' + self.products[0]['name'] + '''</div>
                    <div class="item-spec">黑色 / M</div>
                    <div class="item-price-row">
                        <span class="item-price">¥''' + str(self.products[0]['current_price']) + '''</span>
                        <span class="item-qty">x1</span>
                    </div>
                </div>
            </div>
            <div class="checkout-row">
                <span>配送方式</span>
                <span>快递免邮 ></span>
            </div>
            <div class="checkout-row">
                <span>店铺优惠</span>
                <span class="highlight">-¥20 ></span>
            </div>
            <div class="checkout-row">
                <span>订单备注</span>
                <input type="text" placeholder="选填，请与商家协商一致">
            </div>
            <div class="shop-total">
                <span>小计:</span>
                <span class="price">¥''' + str(self.products[0]['current_price'] - 20) + '''</span>
            </div>
        </div>
    </section>

    <!-- 支付方式 -->
    <section class="payment-section">
        <div class="container">
            <h3>支付方式</h3>
            <div class="payment-list">
                <label class="payment-item active">
                    <span class="payment-icon">💳</span>
                    <span class="payment-name">微信支付</span>
                    <input type="radio" name="payment" value="wechat" checked>
                    <span class="payment-check">✓</span>
                </label>
                <label class="payment-item">
                    <span class="payment-icon">💰</span>
                    <span class="payment-name">支付宝</span>
                    <input type="radio" name="payment" value="alipay">
                    <span class="payment-check">○</span>
                </label>
            </div>
        </div>
    </section>

    <!-- 底部结算栏 -->
    <div class="checkout-footer">
        <div class="container">
            <div class="total-amount">
                <span>合计:</span>
                <span class="amount">¥''' + str(self.products[0]['current_price'] - 20) + '''</span>
            </div>
            <button class="btn-submit-order" onclick="submitOrder()">提交订单</button>
        </div>
    </div>

    <script src="data.js"></script>
    <script src="app.js"></script>
</body>
</html>'''
        
        (self.output_dir / 'checkout.html').write_text(html, encoding='utf-8')
        print("✅ 生成: checkout.html")
    
    def generate_css(self):
        """生成CSS样式"""
        # CSS内容太长，这里简化展示核心部分
        css = '''/* ====================
   电商平台原型样式 - V6完整版
   ==================== */

:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --primary-color: #667eea;
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --danger: #ff4757;
    --success: #2ed573;
    --warning: #ffa502;
    --text-primary: #1a1a2e;
    --text-secondary: #4a4a6a;
    --text-muted: #8b8b9a;
    --bg-primary: #f8f9fc;
    --bg-card: #ffffff;
    --border-color: #e8eaf2;
    --shadow: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 16px 48px rgba(0,0,0,0.16);
    --radius: 12px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    padding-bottom: 80px;
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

/* 顶部导航 */
.header {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 100;
}

.header-content {
    display: flex;
    align-items: center;
    padding: 12px 20px;
    gap: 15px;
}

.logo {
    font-size: 22px;
    font-weight: 800;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* 搜索框 */
.search-box {
    flex: 1;
    max-width: 450px;
    position: relative;
}

.search-box input {
    width: 100%;
    padding: 12px 45px 12px 20px;
    background: var(--bg-primary);
    border: 2px solid transparent;
    border-radius: 30px;
    outline: none;
    font-size: 14px;
    transition: var(--transition);
}

.search-box input:focus {
    background: var(--bg-card);
    border-color: var(--primary-color);
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.search-box button {
    position: absolute;
    right: 6px;
    top: 50%;
    transform: translateY(-50%);
    padding: 8px 18px;
    background: var(--primary-gradient);
    color: white;
    border: none;
    border-radius: 24px;
    cursor: pointer;
}

/* Banner */
.banner {
    position: relative;
    height: 400px;
    overflow: hidden;
    border-radius: 0 0 24px 24px;
}

.banner-item {
    min-width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    position: relative;
}

.banner-content {
    text-align: center;
    z-index: 1;
}

.banner-tag {
    display: inline-block;
    padding: 6px 16px;
    background: rgba(255,255,255,0.2);
    border-radius: 20px;
    font-size: 13px;
    margin-bottom: 16px;
}

.banner-content h2 {
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 12px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.banner-btn {
    padding: 14px 32px;
    background: white;
    color: var(--primary-color);
    border: none;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

/* 商品卡片 */
.product-card {
    background: var(--bg-card);
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    cursor: pointer;
    transition: var(--transition);
}

.product-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-lg);
}

.product-img-wrapper {
    position: relative;
    overflow: hidden;
}

.product-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    transition: var(--transition);
}

.product-card:hover .product-img {
    transform: scale(1.05);
}

.product-badge {
    position: absolute;
    top: 10px;
    left: 10px;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
    color: white;
}

.product-badge.new { background: var(--success); }
.product-badge.hot { background: var(--danger); }

.product-info { padding: 16px; }

.product-tags {
    display: flex;
    gap: 6px;
    margin-bottom: 8px;
}

.product-tag {
    padding: 2px 8px;
    background: rgba(102, 126, 234, 0.1);
    color: var(--primary-color);
    border-radius: 4px;
    font-size: 11px;
}

.current-price {
    color: var(--danger);
    font-size: 20px;
    font-weight: 800;
}

.original-price {
    color: var(--text-muted);
    font-size: 13px;
    text-decoration: line-through;
    margin-left: 6px;
}

/* 底部导航 */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    display: flex;
    justify-content: space-around;
    padding: 12px 0 24px;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
    z-index: 100;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: var(--text-muted);
    font-size: 11px;
    padding: 4px 16px;
    border-radius: 12px;
    transition: var(--transition);
}

.nav-item.active {
    color: var(--primary-color);
    background: rgba(102, 126, 234, 0.1);
}

.nav-icon { font-size: 24px; margin-bottom: 4px; }

/* 弹窗 */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1000;
}

.modal.active { display: block; }

.modal-mask {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
}

.modal-content {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: white;
    border-radius: 24px 24px 0 0;
    padding: 24px;
    animation: slideUp 0.3s ease;
    max-height: 85vh;
    overflow-y: auto;
}

@keyframes slideUp {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.modal-header h3 {
    font-size: 18px;
    font-weight: 700;
}

.modal-close {
    font-size: 24px;
    color: var(--text-muted);
    cursor: pointer;
}

/* Toast */
.toast {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(0,0,0,0.8);
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    z-index: 2000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
}

.toast.show { opacity: 1; }

/* 加载更多 */
.load-more {
    text-align: center;
    padding: 30px;
}

.btn-load-more {
    padding: 12px 40px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 24px;
    color: var(--text-secondary);
    cursor: pointer;
    transition: var(--transition);
}

.btn-load-more:hover {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

/* 筛选标签 */
.filter-tabs {
    display: flex;
    gap: 12px;
}

.filter-tabs .tab {
    padding: 6px 16px;
    background: var(--bg-primary);
    border-radius: 20px;
    font-size: 13px;
    color: var(--text-secondary);
    cursor: pointer;
    transition: var(--transition);
}

.filter-tabs .tab.active {
    background: var(--primary-color);
    color: white;
}

/* 响应式 */
@media (max-width: 768px) {
    .product-grid { grid-template-columns: repeat(2, 1fr); }
    .banner { height: 280px; }
    .banner-content h2 { font-size: 28px; }
}
'''
        
        (self.output_dir / 'styles.css').write_text(css, encoding='utf-8')
        print("✅ 生成: styles.css")
    
    def generate_data_js(self):
        """生成数据JS文件"""
        js = '''// 项目数据
const PROJECT_CONFIG = ''' + json.dumps({
            "name": self.project_name,
            "version": "6.0.0",
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }, ensure_ascii=False, indent=2) + ''';

const PRODUCTS = ''' + json.dumps(self.products, ensure_ascii=False, indent=2) + ''';

const CART_DATA = ''' + json.dumps(self.cart_data, ensure_ascii=False, indent=2) + ''';

const COUPONS = ''' + json.dumps(self.coupons, ensure_ascii=False, indent=2) + ''';

const ADDRESSES = ''' + json.dumps(self.addresses, ensure_ascii=False, indent=2) + ''';

const REVIEWS = ''' + json.dumps(self.reviews, ensure_ascii=False, indent=2) + ''';

const USER_INFO = ''' + json.dumps(self.user_info, ensure_ascii=False, indent=2) + ''';

const CATEGORIES = ''' + json.dumps(self.categories, ensure_ascii=False, indent=2) + ''';
'''
        
        (self.output_dir / 'data.js').write_text(js, encoding='utf-8')
        print("✅ 生成: data.js")
    
    def generate_app_js(self):
        """生成应用JS文件"""
        js = '''// 电商原型 - 完整交互脚本

// ====================
// 全局状态
// ====================
let cartCount = CART_DATA.reduce((sum, shop) => sum + shop.products.length, 0);
let isEditMode = false;
let selectedSku = { color: null, size: null, quantity: 1 };
let isFavorite = false;
let selectedCoupon = 0;
let currentFilter = 'all';

// ====================
// 工具函数
// ====================
function showToast(message, duration = 2000) {
    const toast = document.getElementById('toast');
    if (toast) {
        toast.textContent = message;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), duration);
    }
}

function formatPrice(price) {
    return '¥' + parseFloat(price).toFixed(2);
}

// ====================
// 页面初始化
// ====================
document.addEventListener('DOMContentLoaded', function() {
    initPage();
});

function initPage() {
    const path = window.location.pathname;
    
    if (path.includes('index') || path === '/' || !path.includes('.html')) {
        initIndexPage();
    }
    if (path.includes('product-detail')) {
        initProductDetailPage();
    }
    if (path.includes('cart')) {
        initCartPage();
    }
    if (path.includes('user')) {
        initUserPage();
    }
    if (path.includes('checkout')) {
        initCheckoutPage();
    }
}

// ====================
// 首页功能
// ====================
function initIndexPage() {
    initBannerSlider();
    startSeckillCountdown();
    updateCartBadge();
    
    // 搜索建议
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('focus', () => {
            document.getElementById('searchSuggestions')?.classList.add('show');
        });
    }
}

function initBannerSlider() {
    const slider = document.getElementById('bannerSlider');
    if (!slider) return;
    
    let currentSlide = 0;
    const items = slider.querySelectorAll('.banner-item');
    const indicators = document.querySelectorAll('.banner-indicators span');
    
    if (items.length <= 1) return;
    
    setInterval(() => {
        currentSlide = (currentSlide + 1) % items.length;
        slider.style.transform = `translateX(-${currentSlide * 100}%)`;
        indicators.forEach((ind, i) => ind.classList.toggle('active', i === currentSlide));
    }, 4000);
}

function goToSlide(index) {
    const slider = document.getElementById('bannerSlider');
    const indicators = document.querySelectorAll('.banner-indicators span');
    if (slider) {
        slider.style.transform = `translateX(-${index * 100}%)`;
        indicators.forEach((ind, i) => ind.classList.toggle('active', i === index));
    }
}

function startSeckillCountdown() {
    let hours = 2, minutes = 45, seconds = 30;
    
    setInterval(() => {
        seconds--;
        if (seconds < 0) { seconds = 59; minutes--; }
        if (minutes < 0) { minutes = 59; hours--; }
        if (hours < 0) { hours = 2; minutes = 45; seconds = 30; }
        
        const hEl = document.getElementById('hours');
        const mEl = document.getElementById('minutes');
        const sEl = document.getElementById('seconds');
        
        if (hEl) hEl.textContent = String(hours).padStart(2, '0');
        if (mEl) mEl.textContent = String(minutes).padStart(2, '0');
        if (sEl) sEl.textContent = String(seconds).padStart(2, '0');
    }, 1000);
}

function updateCartBadge() {
    const badge = document.getElementById('cartBadge');
    if (badge) {
        badge.textContent = cartCount;
        badge.style.display = cartCount > 0 ? 'flex' : 'none';
    }
}

function handleSearch(e) {
    if (e.key === 'Enter') {
        search();
    }
}

function search() {
    const input = document.getElementById('searchInput');
    const keyword = input?.value.trim();
    if (keyword) {
        showToast(`搜索: ${keyword}`);
    } else {
        showToast('请输入搜索关键词');
    }
}

function filterProducts(type, el) {
    document.querySelectorAll('.filter-tabs .tab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
    
    const cards = document.querySelectorAll('.product-card');
    cards.forEach(card => {
        if (type === 'all' || card.dataset.category === type) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function loadMoreProducts() {
    const btn = document.querySelector('.btn-load-more');
    const spinner = btn?.querySelector('.loading-spinner');
    const text = btn?.querySelector('span:first-child');
    
    if (btn && spinner && text) {
        text.style.display = 'none';
        spinner.style.display = 'inline';
        
        setTimeout(() => {
            text.style.display = 'inline';
            spinner.style.display = 'none';
            showToast('已加载更多商品');
        }, 1000);
    }
}

// ====================
// 商品详情页功能
// ====================
function initProductDetailPage() {
    initGallerySlider();
    initSkuSelection();
    initScrollHeader();
}

function initGallerySlider() {
    const slider = document.getElementById('gallerySlider');
    if (!slider) return;
    
    let currentSlide = 0;
    const items = slider.querySelectorAll('.gallery-item');
    const indicators = document.querySelectorAll('.gallery-indicators span');
    const counter = document.getElementById('currentSlide');
    
    if (items.length <= 1) return;
    
    let startX = 0;
    
    slider.addEventListener('touchstart', (e) => startX = e.touches[0].clientX);
    
    slider.addEventListener('touchend', (e) => {
        const diff = startX - e.changedTouches[0].clientX;
        if (Math.abs(diff) > 50) {
            if (diff > 0 && currentSlide < items.length - 1) currentSlide++;
            else if (diff < 0 && currentSlide > 0) currentSlide--;
            
            slider.style.transform = `translateX(-${currentSlide * 100}%)`;
            indicators.forEach((ind, i) => ind.classList.toggle('active', i === currentSlide));
            if (counter) counter.textContent = currentSlide + 1;
        }
    });
}

function initScrollHeader() {
    const header = document.getElementById('detailHeader');
    const tabs = document.getElementById('headerTabs');
    if (!header) return;
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            header.classList.add('scrolled');
            if (tabs) tabs.style.opacity = '1';
        } else {
            header.classList.remove('scrolled');
            if (tabs) tabs.style.opacity = '0';
        }
    });
}

function scrollToSection(section) {
    const el = document.getElementById(section);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
    }
}

function initSkuSelection() {
    const firstColor = document.querySelector('.sku-option-values .sku-value');
    const sizeContainer = document.querySelectorAll('.sku-option-values')[1];
    const firstSize = sizeContainer?.querySelector('.sku-value');
    
    if (firstColor) selectedSku.color = firstColor.textContent;
    if (firstSize) selectedSku.size = firstSize.textContent;
    
    updateSkuDisplay();
}

function updateSkuDisplay() {
    const text = selectedSku.color && selectedSku.size 
        ? `${selectedSku.color} / ${selectedSku.size}，${selectedSku.quantity}件`
        : '请选择规格';
    
    const displayEl = document.getElementById('selectedSkuText');
    const skuSelectedEl = document.getElementById('skuSelected');
    
    if (displayEl) displayEl.textContent = text;
    if (skuSelectedEl) skuSelectedEl.textContent = `已选: ${selectedSku.color}、${selectedSku.size}`;
}

function showSkuModal() {
    document.getElementById('skuModal')?.classList.add('active');
}

function closeSkuModal() {
    document.getElementById('skuModal')?.classList.remove('active');
}

function selectSku(type, value, el) {
    const container = el.closest('.sku-option-values');
    container.querySelectorAll('.sku-value').forEach(v => v.classList.remove('active'));
    el.classList.add('active');
    
    selectedSku[type] = value;
    updateSkuDisplay();
}

function increaseQty() {
    const input = document.getElementById('quantityInput');
    if (!input) return;
    
    const max = parseInt(input.max) || 99;
    selectedSku.quantity = parseInt(input.value) || 1;
    
    if (selectedSku.quantity < max) {
        selectedSku.quantity++;
        input.value = selectedSku.quantity;
        updateSkuDisplay();
    }
}

function decreaseQty() {
    const input = document.getElementById('quantityInput');
    if (!input) return;
    
    selectedSku.quantity = parseInt(input.value) || 1;
    
    if (selectedSku.quantity > 1) {
        selectedSku.quantity--;
        input.value = selectedSku.quantity;
        updateSkuDisplay();
    }
}

function confirmSku() {
    closeSkuModal();
    if (selectedSku.color && selectedSku.size) {
        showToast(`已选择: ${selectedSku.color}、${selectedSku.size} × ${selectedSku.quantity}`);
    }
}

function addToCart() {
    showSkuModal();
    setTimeout(() => {
        cartCount += selectedSku.quantity;
        updateCartBadge();
        showToast('已加入购物车');
    }, 500);
}

function buyNow() {
    location.href = 'checkout.html';
}

function toggleFavorite() {
    isFavorite = !isFavorite;
    const icon = document.getElementById('favoriteIcon');
    const text = document.getElementById('favoriteText');
    
    if (icon && text) {
        icon.textContent = isFavorite ? '💖' : '⭐';
        text.textContent = isFavorite ? '已收藏' : '收藏';
    }
    
    showToast(isFavorite ? '已添加到收藏夹' : '已取消收藏');
}

function showCouponModal() {
    document.getElementById('couponModal')?.classList.add('active');
}

function closeCouponModal() {
    document.getElementById('couponModal')?.classList.remove('active');
}

function claimCoupon(btn, amount) {
    btn.textContent = '已领取';
    btn.disabled = true;
    btn.style.background = '#ccc';
    showToast(`优惠券领取成功！¥${amount}`);
}

function filterReviews(type, el) {
    document.querySelectorAll('.review-tags .tag').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
    showToast(`筛选: ${el.textContent}`);
}

function goToAllReviews() {
    showToast('查看全部评价');
}

// ====================
// 购物车功能
// ====================
function initCartPage() {
    updateCartTotal();
    bindCartEvents();
    checkEmptyCart();
}

function bindCartEvents() {
    document.querySelectorAll('.shop-checkbox').forEach(cb => {
        cb.addEventListener('change', function() {
            const shop = this.closest('.cart-shop');
            shop.querySelectorAll('.item-checkbox').forEach(item => {
                item.checked = this.checked;
            });
            updateCartTotal();
        });
    });
    
    document.querySelectorAll('.item-checkbox').forEach(cb => {
        cb.addEventListener('change', function() {
            updateShopCheckbox(this);
            updateCartTotal();
        });
    });
}

function updateShopCheckbox(itemCb) {
    const shop = itemCb.closest('.cart-shop');
    const allItems = shop.querySelectorAll('.item-checkbox');
    const checkedItems = shop.querySelectorAll('.item-checkbox:checked');
    
    const shopCb = shop.querySelector('.shop-checkbox');
    if (shopCb) {
        shopCb.checked = allItems.length === checkedItems.length;
    }
}

function updateCartTotal() {
    let total = 0;
    let count = 0;
    let discount = 0;
    
    document.querySelectorAll('.cart-item').forEach(item => {
        const checkbox = item.querySelector('.item-checkbox');
        if (checkbox && checkbox.checked) {
            const priceEl = item.querySelector('.cart-item-price');
            const qtyEl = item.querySelector('.qty-input');
            
            const price = parseFloat(priceEl?.textContent?.replace('¥', '') || 0);
            const qty = parseInt(qtyEl?.value || 1);
            
            total += price * qty;
            count += qty;
        }
    });
    
    // 应用优惠券
    if (selectedCoupon > 0) {
        discount = selectedCoupon;
        total = Math.max(0, total - discount);
    }
    
    const totalEl = document.getElementById('totalPrice');
    const btnEl = document.getElementById('btnSettle');
    const discountEl = document.getElementById('discountInfo');
    
    if (totalEl) totalEl.textContent = formatPrice(total);
    if (btnEl) btnEl.textContent = `结算(${count})`;
    if (discountEl) {
        discountEl.textContent = discount > 0 ? `已优惠 ${formatPrice(discount)}` : '';
        discountEl.style.display = discount > 0 ? 'block' : 'none';
    }
}

function changeQty(btn, delta) {
    const item = btn.closest('.cart-item');
    const input = item?.querySelector('.qty-input');
    if (!input) return;
    
    let val = parseInt(input.value) || 1;
    const max = parseInt(input.max) || 99;
    
    val += delta;
    if (val >= 1 && val <= max) {
        input.value = val;
        updateCartTotal();
    }
}

function toggleSelectAll() {
    const selectAll = document.getElementById('selectAll');
    if (!selectAll) return;
    
    document.querySelectorAll('.shop-checkbox, .item-checkbox').forEach(cb => {
        cb.checked = selectAll.checked;
    });
    
    updateCartTotal();
}

function toggleEditMode() {
    isEditMode = !isEditMode;
    const editBtn = document.getElementById('editBtn');
    const settleSection = document.getElementById('settleSection');
    const deleteSection = document.getElementById('deleteSection');
    
    if (editBtn) editBtn.textContent = isEditMode ? '完成' : '管理';
    if (settleSection) settleSection.style.display = isEditMode ? 'none' : 'flex';
    if (deleteSection) deleteSection.style.display = isEditMode ? 'flex' : 'none';
}

function deleteSelected() {
    const selected = document.querySelectorAll('.item-checkbox:checked');
    if (selected.length === 0) {
        showToast('请选择要删除的商品');
        return;
    }
    
    if (confirm(`确定要删除选中的 ${selected.length} 个商品吗？`)) {
        selected.forEach(cb => {
            const item = cb.closest('.cart-item');
            if (item) {
                item.remove();
                cartCount--;
            }
        });
        updateCartBadge();
        updateCartTotal();
        checkEmptyCart();
        showToast('删除成功');
    }
}

function moveToFavorite() {
    showToast('已移入收藏夹');
}

function checkEmptyCart() {
    const items = document.querySelectorAll('.cart-item');
    const emptyCart = document.getElementById('emptyCart');
    const cartContent = document.querySelector('.cart-content .container');
    
    if (items.length === 0 && emptyCart && cartContent) {
        cartContent.style.display = 'none';
        emptyCart.style.display = 'block';
    }
}

function showAddressModal() {
    document.getElementById('addressModal')?.classList.add('active');
}

function closeAddressModal() {
    document.getElementById('addressModal')?.classList.remove('active');
}

function selectAddress(addressId) {
    showToast('地址切换成功');
    closeAddressModal();
}

function addNewAddress() {
    showToast('添加新地址');
}

function showCartCouponModal(shopId) {
    document.getElementById('cartCouponModal')?.classList.add('active');
}

function closeCartCouponModal() {
    document.getElementById('cartCouponModal')?.classList.remove('active');
}

function selectCartCoupon(el, amount) {
    document.querySelectorAll('.coupon-item').forEach(item => {
        item.classList.remove('selected');
        item.querySelector('.coupon-select').textContent = '○';
    });
    
    el.classList.add('selected');
    el.querySelector('.coupon-select').textContent = '✓';
    
    selectedCoupon = amount;
    updateCartTotal();
    setTimeout(closeCartCouponModal, 300);
    showToast(`已选择优惠券 -¥${amount}`);
}

function goCheckout() {
    const selected = document.querySelectorAll('.item-checkbox:checked');
    if (selected.length === 0) {
        showToast('请选择要结算的商品');
        return;
    }
    location.href = 'checkout.html';
}

// ====================
// 用户中心功能
// ====================
function initUserPage() {
    // 用户页面初始化
}

function editProfile() {
    showToast('编辑个人资料');
}

function goToOrders(status) {
    showToast(`查看订单: ${status}`);
}

function goToCollection() {
    showToast('我的收藏');
}

function goToHistory() {
    showToast('浏览足迹');
}

function goToCoupons() {
    showToast('我的优惠券');
}

function goToPoints() {
    showToast('我的积分');
}

function goToAddress() {
    showToast('收货地址管理');
}

function goToService() {
    showToast('客服中心');
}

function goToHelp() {
    showToast('帮助中心');
}

function goToSettings() {
    showToast('设置');
}

function goToAbout() {
    showToast('关于我们');
}

function showMessage() {
    showToast('消息中心');
}

// ====================
// 订单确认功能
// ====================
function initCheckoutPage() {
    // 结算页面初始化
}

function submitOrder() {
    showToast('订单提交成功！');
    setTimeout(() => {
        location.href = 'user.html';
    }, 1500);
}

// ====================
// 通用导航功能
// ====================
function goToIndex() {
    location.href = 'index.html';
}

function goToCart() {
    location.href = 'cart.html';
}

function goToUser() {
    location.href = 'user.html';
}

function goToProduct(productId) {
    location.href = `product-detail.html?id=${productId}`;
}

function goToCategory(categoryId) {
    showToast(`进入分类: ${categoryId}`);
}

function goToShop(shopId) {
    showToast(`进入店铺: ${shopId}`);
}

function goToPromotion(type) {
    showToast(`查看活动: ${type}`);
}

function contactService() {
    showToast('联系客服');
}

function shareProduct() {
    showToast('分享商品');
}

function showMoreMenu() {
    showToast('更多选项');
}

function showFilter() {
    showToast('筛选商品');
}

function selectSidebarCat(index, el) {
    document.querySelectorAll('.sidebar-item').forEach(item => item.classList.remove('active'));
    el.classList.add('active');
}

function selectCategory(catId) {
    showToast(`选择分类: ${catId}`);
}

function filterBySubCat(subCat) {
    showToast(`筛选: ${subCat}`);
}
'''
        
        (self.output_dir / 'app.js').write_text(js, encoding='utf-8')
        print("✅ 生成: app.js")


# ===========================
# 主程序
# ===========================

def main():
    if len(sys.argv) < 2:
        project_name = "电商平台"
        output_dir = "./output"
    else:
        project_name = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output"
    
    generator = HtmlPrototypeGenerator(project_name, output_dir)
    generator.generate()


if __name__ == "__main__":
    main()
