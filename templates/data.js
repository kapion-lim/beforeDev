/**
 * 假数据生成器
 * 自动生成逼真的电商数据
 */

// 项目配置
const PROJECT_CONFIG = {
    name: '{{PROJECT_NAME}}',
    version: '1.0.0'
};

// ===========================
// 假数据生成函数
// ===========================

// 生成随机ID
function generateId() {
    return 'id_' + Math.random().toString(36).substr(2, 9);
}

// 生成随机整数
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// 生成随机字符串
function randomString(length) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}

// 随机选择数组元素
function randomPick(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// ===========================
// 商品数据
// ===========================

const PRODUCT_NAMES = [
    '2024新款时尚休闲卫衣男', '纯棉宽松T恤女装', '复古刺绣连衣裙夏', 
    '运动休闲鞋男透气', '真皮女士手提包', '智能运动手表心率监测',
    '无线蓝牙耳机降噪', '便携式移动电源20000毫安', '高清智能摄像头家用',
    '全自动滚筒洗衣机', '双门小型冰箱静音', '智能扫地机器人吸尘器',
    '轻奢水晶吊灯客厅', '北欧实木餐桌椅组合', '舒适乳胶床垫1.8米'
];

const PRODUCT_IMAGES = [
    'https://picsum.photos/400/400?random=1',
    'https://picsum.photos/400/400?random=2',
    'https://picsum.photos/400/400?random=3',
    'https://picsum.photos/400/400?random=4',
    'https://picsum.photos/400/400?random=5',
    'https://picsum.photos/400/400?random=6',
    'https://picsum.photos/400/400?random=7',
    'https://picsum.photos/400/400?random=8'
];

const BANNER_IMAGES = [
    'https://picsum.photos/750/400?random=10',
    'https://picsum.photos/750/400?random=11',
    'https://picsum.photos/750/400?random=12',
    'https://picsum.photos/750/400?random=13'
];

const COLORS = ['黑色', '白色', '红色', '蓝色', '灰色', '粉色', '绿色'];
const SIZES = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];

// 生成商品列表
function generateProducts(count = 8) {
    const products = [];
    for (let i = 0; i < count; i++) {
        const originalPrice = randomInt(99, 999);
        const discount = randomPick([0.8, 0.85, 0.9, 0.95]);
        const currentPrice = Math.round(originalPrice * discount);
        
        products.push({
            id: generateId(),
            name: PRODUCT_NAMES[i % PRODUCT_NAMES.length],
            image: PRODUCT_IMAGES[i % PRODUCT_IMAGES.length],
            originalPrice: originalPrice,
            currentPrice: currentPrice,
            soldCount: randomInt(100, 10000),
            goodRate: randomInt(90, 99),
            colors: COLORS.slice(0, randomInt(2, 4)),
            sizes: SIZES.slice(0, randomInt(3, 6)),
            stock: randomInt(10, 500)
        });
    }
    return products;
}

// ===========================
// 购物车数据
// ===========================

const SHOP_NAMES = [
    '优品数码专营店', '时尚潮流服饰馆', '品质生活家居馆', 
    '美妆护肤旗舰店', '运动户外专营店'
];

function generateCartData() {
    const shops = [];
    const shopCount = randomInt(1, 3);
    
    for (let i = 0; i < shopCount; i++) {
        const products = [];
        const productCount = randomInt(1, 3);
        
        for (let j = 0; j < productCount; j++) {
            const product = generateProducts(1)[0];
            products.push({
                id: generateId(),
                ...product,
                quantity: randomInt(1, 5),
                selected: true
            });
        }
        
        shops.push({
            id: generateId(),
            name: SHOP_NAMES[i % SHOP_NAMES.length],
            products: products
        });
    }
    
    return shops;
}

// ===========================
// 优惠券数据
// ===========================

const COUPONS = [
    { name: '新人专享券', amount: 20, threshold: 99, type: '新人' },
    { name: '满减优惠券', amount: 50, threshold: 299, type: '满减' },
    { name: '店铺专用券', amount: 10, threshold: 59, type: '店铺' },
    { name: '限时秒杀券', amount: 30, threshold: 199, type: '秒杀' },
    { name: '生日特惠券', amount: 100, threshold: 499, type: '生日' }
];

function generateCoupons(count = 5) {
    return COUPONS.slice(0, count).map(coupon => ({
        ...coupon,
        id: generateId(),
        receiveTime: new Date().toLocaleDateString(),
        expireTime: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toLocaleDateString()
    }));
}

// ===========================
// 地址数据
// ===========================

const CITIES = ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '西安', '南京', '重庆'];
const DISTRICTS = ['朝阳区', '海淀区', '浦东新区', '天河区', '南山区', '西湖区', '武侯区', '雁塔区', '玄武区', '渝中区'];
const STREETS = ['中关村大街', '望京SOHO', '陆家嘴金融中心', '天河城购物中心', '科技园南区', '武林广场', '春熙路', '大唐不夜城', '新街口', '解放碑'];

function generateAddress() {
    const city = randomPick(CITIES);
    const district = randomPick(DISTRICTS);
    const street = randomPick(STREETS);
    const detail = `具体门牌号${randomInt(1, 999)}号`;
    
    return {
        id: generateId(),
        name: randomPick(['张三', '李四', '王五', '赵六']),
        phone: `1${randomInt(3, 9)}${randomInt(100000000, 999999999)}`,
        province: city === '北京' || city === '上海' ? city + '市' : city + '省',
        city: city + '市',
        district: district,
        address: city + district + street + detail,
        isDefault: Math.random() > 0.7
    };
}

// ===========================
// 订单数据
// ===========================

const ORDER_STATUS = [
    { status: 'pending_payment', name: '待付款', color: '#ff9800' },
    { status: 'pending_shipment', name: '待发货', color: '#2196f3' },
    { status: 'pending_receipt', name: '待收货', color: '#9c27b0' },
    { status: 'completed', name: '已完成', color: '#4caf50' },
    { status: 'cancelled', name: '已取消', color: '#999' }
];

function generateOrder() {
    const products = generateProducts(randomInt(1, 4));
    const status = randomPick(ORDER_STATUS);
    const totalAmount = products.reduce((sum, p) => sum + p.currentPrice * p.quantity, 0);
    
    return {
        id: 'ORD' + Date.now(),
        orderNo: '2024' + randomString(12),
        status: status,
        products: products,
        totalAmount: totalAmount,
        freight: totalAmount >= 99 ? 0 : 10,
        discount: randomInt(0, 50),
        address: generateAddress(),
        createTime: new Date(Date.now() - randomInt(0, 7) * 24 * 60 * 60 * 1000).toLocaleString(),
        payTime: status.status !== 'pending_payment' ? new Date(Date.now() - randomInt(0, 5) * 24 * 60 * 60 * 1000).toLocaleString() : null
    };
}

// ===========================
// 用户数据
// ===========================

function generateUser() {
    return {
        id: generateId(),
        name: randomPick(['电商达人', '购物狂人', '品质生活家', '时尚买手', '精明消费者']),
        avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${randomString(8)}`,
        phone: `1${randomInt(3, 9)}${randomInt(100000000, 999999999)}`,
        level: randomPick(['普通会员', '银牌会员', '金牌会员', '钻石会员']),
        points: randomInt(100, 10000),
        coupons: randomInt(0, 20),
        unpaidOrders: randomInt(0, 3),
        unpaidShipment: randomInt(0, 5),
        unpaidReceipt: randomInt(0, 2)
    };
}

// ===========================
// 评价数据
// ===========================

const REVIEW_CONTENTS = [
    '质量很好，包装也很精美，会回购的！',
    '物流很快，客服态度很好，满意！',
    '性价比很高，比实体店便宜多了，推荐购买！',
    '颜色和图片一致，没有色差，很满意！',
    '穿上去很舒服，尺码标准，下次还来！',
    '宝贝收到了，质量很好，价格实惠，值得购买！',
    '非常满意的一次购物体验，店家服务周到！',
    '东西不错，好评！',
    '比想象中还要好，真的太喜欢了！',
    '整体不错，就是快递有点慢'
];

function generateReviews(count = 10) {
    const reviews = [];
    for (let i = 0; i < count; i++) {
        reviews.push({
            id: generateId(),
            userName: '用户' + randomString(6),
            avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${randomString(8)}`,
            rating: randomInt(4, 5),
            content: randomPick(REVIEW_CONTENTS),
            images: Array(randomInt(0, 3)).fill(0).map(() => 
                `https://picsum.photos/100/100?random=${randomInt(100, 999)}`
            ),
            spec: `${randomPick(COLORS)}/${randomPick(SIZES)}`,
            createTime: new Date(Date.now() - randomInt(1, 30) * 24 * 60 * 60 * 1000).toLocaleString()
        });
    }
    return reviews;
}

// ===========================
// 导出数据
// ===========================

window.FakeData = {
    config: PROJECT_CONFIG,
    products: {
        list: generateProducts,
        names: PRODUCT_NAMES,
        images: PRODUCT_IMAGES
    },
    cart: {
        generate: generateCartData
    },
    coupons: {
        list: generateCoupons
    },
    address: {
        generate: generateAddress
    },
    order: {
        generate: generateOrder,
        status: ORDER_STATUS
    },
    user: {
        generate: generateUser
    },
    reviews: {
        generate: generateReviews
    },
    banners: BANNER_IMAGES,
    utils: {
        generateId,
        randomInt,
        randomPick
    }
};
