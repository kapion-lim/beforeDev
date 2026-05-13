/**
 * 电商原型 - 交互脚本
 */

// ===========================
// 全局变量
// ===========================

let isFavorite = false;
let selectedSku = {
    color: null,
    size: null
};
let currentQuantity = 1;
let cartData = [];
let editMode = false;

// ===========================
// 页面初始化
// ===========================

function initPage() {
    // 根据页面类型初始化
    const pageName = getCurrentPage();
    
    switch(pageName) {
        case 'index':
            initIndexPage();
            break;
        case 'product-detail':
            initProductDetailPage();
            break;
        case 'cart':
            initCartPage();
            break;
    }
}

function getCurrentPage() {
    const path = window.location.pathname;
    if (path.includes('product-detail')) return 'product-detail';
    if (path.includes('cart')) return 'cart';
    return 'index';
}

// ===========================
// 首页初始化
// ===========================

function initIndexPage() {
    renderBanners();
    renderQuickEntries();
    renderSeckillProducts();
    renderRecommendProducts();
    initSearch();
}

// Banner 轮播
function renderBanners() {
    const slider = document.getElementById('bannerSlider');
    const indicators = document.querySelector('.banner-indicators');
    
    if (!slider || !indicators) return;
    
    const banners = FakeData.banners;
    
    // 渲染轮播图
    slider.innerHTML = banners.map((img, i) => `
        <div class="banner-item" style="background-image: url('${img}')">
            <div style="width:100%;height:100%;background:linear-gradient(135deg,rgba(255,107,53,0.1),rgba(247,37,133,0.1))"></div>
        </div>
    `).join('');
    
    // 渲染指示器
    indicators.innerHTML = banners.map((_, i) => `
        <span class="${i === 0 ? 'active' : ''}" onclick="goToSlide(${i})"></span>
    `).join('');
    
    // 自动轮播
    let currentSlide = 0;
    setInterval(() => {
        currentSlide = (currentSlide + 1) % banners.length;
        slider.style.transform = `translateX(-${currentSlide * 100}%)`;
        updateIndicators(currentSlide);
    }, 3000);
}

function goToSlide(index) {
    const slider = document.getElementById('bannerSlider');
    slider.style.transform = `translateX(-${index * 100}%)`;
    updateIndicators(index);
}

function updateIndicators(activeIndex) {
    const indicators = document.querySelectorAll('.banner-indicators span');
    indicators.forEach((ind, i) => {
        ind.classList.toggle('active', i === activeIndex);
    });
}

// 快捷入口
function renderQuickEntries() {
    const grid = document.querySelector('.quick-grid');
    if (!grid) return;
    
    const entries = [
        { icon: '📱', name: '手机数码', color: '#3498db', link: 'category.html' },
        { icon: '👗', name: '服饰鞋包', color: '#e74c3c', link: 'category.html' },
        { icon: '🏠', name: '家居家装', color: '#f39c12', link: 'category.html' },
        { icon: '💄', name: '美妆护肤', color: '#9b59b6', link: 'category.html' },
        { icon: '⚡', name: '限时秒杀', color: '#e91e63', link: 'seckill.html' },
        { icon: '🎫', name: '优惠券', color: '#ff9800', link: 'coupon.html' },
        { icon: '👶', name: '母婴用品', color: '#00bcd4', link: 'category.html' },
        { icon: '🍔', name: '食品生鲜', color: '#4caf50', link: 'category.html' }
    ];
    
    grid.innerHTML = entries.map(entry => `
        <a href="${entry.link}" class="quick-item">
            <div class="quick-icon" style="background: ${entry.color}">
                ${entry.icon}
            </div>
            <span>${entry.name}</span>
        </a>
    `).join('');
}

// 秒杀商品
function renderSeckillProducts() {
    const container = document.querySelector('.seckill-products');
    if (!container) return;
    
    const products = FakeData.products.list(4);
    
    container.innerHTML = products.map(product => `
        <a href="product-detail.html?id=${product.id}" class="product-card seckill-card">
            <img src="${product.image}" alt="${product.name}" class="product-img">
            <div class="product-info">
                <div class="product-price">¥${product.currentPrice}</div>
                <div class="original-price">¥${product.originalPrice}</div>
            </div>
        </a>
    `).join('');
}

// 推荐商品
function renderRecommendProducts() {
    const containers = document.querySelectorAll('.product-grid');
    const products = FakeData.products.list(8);
    
    containers.forEach(container => {
        container.innerHTML = products.map(product => `
            <a href="product-detail.html?id=${product.id}" class="product-card">
                <img src="${product.image}" alt="${product.name}" class="product-img">
                <div class="product-info">
                    <div class="product-title">${product.name}</div>
                    <div class="product-price">¥${product.currentPrice}</div>
                    <div class="product-meta">已售${product.soldCount}+</div>
                </div>
            </a>
        `).join('');
    });
}

// 搜索功能
function initSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) return;
    
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const keyword = searchInput.value.trim();
            if (keyword) {
                location.href = `product-list.html?keyword=${encodeURIComponent(keyword)}`;
            }
        }
    });
}

// ===========================
// 商品详情页初始化
// ===========================

function initProductDetailPage() {
    renderGallery();
    renderSkuOptions();
    renderReviews();
}

// 商品图库
function renderGallery() {
    const slider = document.getElementById('gallerySlider');
    const indicators = document.querySelector('.gallery-indicators');
    if (!slider) return;
    
    const images = FakeData.products.images.slice(0, 4);
    
    slider.innerHTML = images.map((img, i) => `
        <div class="gallery-item" style="background-image: url('${img}')"></div>
    `).join('');
    
    if (indicators) {
        indicators.innerHTML = images.map((_, i) => `
            <span class="${i === 0 ? 'active' : ''}"></span>
        `).join('');
    }
}

// SKU 选项
function renderSkuOptions() {
    const container = document.querySelector('.sku-body');
    if (!container) return;
    
    const product = FakeData.products.list(1)[0];
    
    container.innerHTML = `
        <div class="sku-option">
            <div class="sku-option-title">颜色</div>
            <div class="sku-option-values">
                ${product.colors.map((color, i) => `
                    <span class="sku-value ${i === 0 ? 'active' : ''}" 
                          onclick="selectSku('color', '${color}', this)">${color}</span>
                `).join('')}
            </div>
        </div>
        <div class="sku-option">
            <div class="sku-option-title">尺码</div>
            <div class="sku-option-values">
                ${product.sizes.map((size, i) => `
                    <span class="sku-value ${i === 0 ? 'active' : ''}" 
                          onclick="selectSku('size', '${size}', this)">${size}</span>
                `).join('')}
            </div>
        </div>
    `;
    
    selectedSku = { color: product.colors[0], size: product.sizes[0] };
}

// SKU 选择
function selectSku(type, value, el) {
    const container = el.closest('.sku-option');
    container.querySelectorAll('.sku-value').forEach(v => v.classList.remove('active'));
    el.classList.add('active');
    selectedSku[type] = value;
    updateSelectedDisplay();
}

function updateSelectedDisplay() {
    const valueEl = document.querySelector('.sku-selector .value');
    if (valueEl) {
        valueEl.textContent = `已选: ${selectedSku.color}、${selectedSku.size}`;
    }
}

// 评价列表
function renderReviews() {
    const container = document.getElementById('productDetail');
    if (!container) return;
    
    const reviews = FakeData.reviews.generate(5);
    
    container.innerHTML += `
        <div class="reviews-section">
            <h3>商品评价</h3>
            ${reviews.map(review => `
                <div class="review-item">
                    <div class="review-header">
                        <img src="${review.avatar}" class="review-avatar">
                        <span class="review-user">${review.userName}</span>
                        <span class="review-rating">${'⭐'.repeat(review.rating)}</span>
                    </div>
                    <div class="review-content">${review.content}</div>
                    <div class="review-meta">
                        <span>${review.spec}</span>
                        <span>${review.createTime}</span>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// 收藏
function toggleFavorite() {
    isFavorite = !isFavorite;
    const btn = document.getElementById('favoriteBtn');
    if (btn) {
        btn.style.color = isFavorite ? '#ff6b35' : '';
        btn.querySelector('span').textContent = isFavorite ? '已收藏' : '收藏';
    }
    alert(isFavorite ? '已添加到收藏夹' : '已取消收藏');
}

// 添加购物车
function addToCart() {
    showSkuModal();
}

// 立即购买
function buyNow() {
    showSkuModal();
}

// SKU 弹窗
function showSkuModal() {
    document.getElementById('skuModal').classList.add('active');
}

function closeSkuModal() {
    document.getElementById('skuModal').classList.remove('active');
}

function increaseQty() {
    const input = document.getElementById('quantityInput');
    const max = parseInt(input.max);
    if (currentQuantity < max) {
        currentQuantity++;
        input.value = currentQuantity;
    }
}

function decreaseQty() {
    if (currentQuantity > 1) {
        currentQuantity--;
        document.getElementById('quantityInput').value = currentQuantity;
    }
}

function confirmSku() {
    closeSkuModal();
    alert(`已选择: ${selectedSku.color}、${selectedSku.size}，数量: ${currentQuantity}`);
}

// 优惠券弹窗
function showCouponModal() {
    document.getElementById('couponModal').classList.add('active');
}

function closeCouponModal() {
    document.getElementById('couponModal').classList.remove('active');
}

// Tab 切换
function switchTab(tabName) {
    const tabs = document.querySelectorAll('.tab-item');
    tabs.forEach(tab => tab.classList.remove('active'));
    event.target.classList.add('active');
    // 根据 tab 切换内容
}

// ===========================
// 购物车初始化
// ===========================

function initCartPage() {
    renderCartItems();
}

function renderCartItems() {
    const containers = document.querySelectorAll('.cart-content .container');
    if (containers.length === 0) return;
    
    const cartData = FakeData.cart.generate();
    
    let html = '';
    let totalPrice = 0;
    let selectedCount = 0;
    
    cartData.forEach(shop => {
        html += `
            <div class="cart-shop">
                <div class="cart-shop-header">
                    <input type="checkbox" checked onchange="toggleShop(this)">
                    <span class="cart-shop-name">${shop.name}</span>
                    <span class="cart-shop-coupon" onclick="location.href='coupon.html'">领券 ></span>
                </div>
        `;
        
        shop.products.forEach(product => {
            const itemTotal = product.currentPrice * product.quantity;
            totalPrice += itemTotal;
            selectedCount++;
            
            html += `
                <div class="cart-item">
                    <input type="checkbox" checked data-price="${product.currentPrice}" data-qty="${product.quantity}">
                    <img src="${product.image}" class="cart-item-img">
                    <div class="cart-item-info">
                        <div class="cart-item-title">${product.name}</div>
                        <div class="cart-item-spec">${product.colors[0]} / ${product.sizes[0]}</div>
                        <div class="cart-item-bottom">
                            <span class="cart-item-price">¥${product.currentPrice}</span>
                            <div class="cart-item-actions">
                                <button onclick="changeQty(this, -1)">-</button>
                                <input type="number" value="${product.quantity}" min="1" max="${product.stock}" onchange="updateItemTotal(this)">
                                <button onclick="changeQty(this, 1)">+</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
    });
    
    containers[0].innerHTML = html;
    
    // 更新底部统计
    document.querySelector('.total-price').textContent = '¥' + totalPrice;
    document.querySelector('.btn-settle').textContent = `结算(${selectedCount})`;
}

function toggleShop(checkbox) {
    const items = checkbox.closest('.cart-shop').querySelectorAll('input[type="checkbox"]');
    items.forEach(item => item.checked = checkbox.checked);
    updateTotal();
}

function toggleSelectAll() {
    const selectAll = document.getElementById('selectAll');
    selectAll.checked = !selectAll.checked;
    document.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = selectAll.checked);
    updateTotal();
}

function changeQty(btn, delta) {
    const input = btn.parentElement.querySelector('input');
    let val = parseInt(input.value) + delta;
    if (val >= 1 && val <= parseInt(input.max)) {
        input.value = val;
        updateItemTotal(input);
    }
}

function updateItemTotal(input) {
    updateTotal();
}

function updateTotal() {
    let total = 0;
    let count = 0;
    document.querySelectorAll('.cart-item input[type="checkbox"]:checked').forEach(cb => {
        const price = parseFloat(cb.dataset.price);
        const qty = parseInt(cb.closest('.cart-item').querySelector('input[type="number"]').value);
        total += price * qty;
        count++;
    });
    
    document.querySelector('.total-price').textContent = '¥' + total;
    document.querySelector('.btn-settle').textContent = `结算(${count})`;
}

function goCheckout() {
    alert('正在跳转订单确认页...');
    location.href = 'checkout.html';
}

// ===========================
// 工具函数
// ===========================

// Toast 提示
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}

// 页面滚动显示头部
window.addEventListener('scroll', function() {
    const header = document.querySelector('.header-fixed');
    if (header) {
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
});
