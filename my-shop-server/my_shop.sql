/*
 Navicat Premium Data Transfer

 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Schema         : my_shop

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 15/02/2024 18:44:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mobile` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'mobile',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像',
  `nickname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '昵称',
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES (1, 'admin', 'admin', NULL, NULL, 0, '2024-01-28 05:56:00.010', '2024-01-28 05:56:00.010', '', '');

-- ----------------------------
-- Table structure for goods_category
-- ----------------------------
DROP TABLE IF EXISTS `goods_category`;
CREATE TABLE `goods_category`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '类目名称',
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '状态 1：展示 0：隐藏',
  `weight` int(11) NOT NULL,
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 56 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_category
-- ----------------------------
INSERT INTO `goods_category` VALUES (1, '水果', 1, 1, 0, '2023-10-26 22:18:52.687', '2023-11-25 10:12:58.198', '', '');
INSERT INTO `goods_category` VALUES (2, '蔬菜', 1, 2, 0, '2023-10-26 22:19:01.720', '2023-11-25 10:12:57.021', '', '');
INSERT INTO `goods_category` VALUES (3, '海鲜', 1, 3, 0, '2023-10-26 22:19:15.862', '2024-02-07 17:18:31.545', '', '');
INSERT INTO `goods_category` VALUES (4, '饮料', 1, 3, 0, '2023-10-26 22:19:27.832', '2023-11-25 10:12:47.299', '', '');
INSERT INTO `goods_category` VALUES (5, '其他', 1, 4, 0, '2023-10-26 22:19:34.000', '2023-12-02 08:09:41.126', '', '');
INSERT INTO `goods_category` VALUES (38, '55', 0, 333, 1, '2023-11-23 10:31:03.550', '2023-11-23 11:51:56.225', '', '');
INSERT INTO `goods_category` VALUES (39, '22', 0, 221, 1, '2023-11-23 10:33:06.105', '2023-11-23 11:51:44.312', '', '');
INSERT INTO `goods_category` VALUES (40, '11', 0, 11, 1, '2023-11-23 11:53:12.608', '2023-11-23 11:53:15.060', '', '');
INSERT INTO `goods_category` VALUES (41, '32', 0, 2, 1, '2023-11-23 11:53:42.262', '2023-11-23 11:55:16.224', '', '');
INSERT INTO `goods_category` VALUES (42, '22', 0, 22, 1, '2023-11-23 11:53:45.077', '2023-11-23 11:53:47.477', '', '');
INSERT INTO `goods_category` VALUES (43, '33', 0, 33, 1, '2023-11-23 11:53:53.005', '2023-11-23 11:55:13.581', '', '');
INSERT INTO `goods_category` VALUES (44, '22', 0, 22, 1, '2023-11-23 11:55:37.771', '2023-11-23 11:55:42.216', '', '');
INSERT INTO `goods_category` VALUES (45, '22', 0, 11, 1, '2023-11-23 11:55:55.175', '2023-11-23 11:55:59.813', '', '');
INSERT INTO `goods_category` VALUES (46, '22', 0, 22, 1, '2023-11-23 11:56:53.744', '2023-11-23 11:56:59.838', '', '');
INSERT INTO `goods_category` VALUES (47, '55', 0, 55, 1, '2023-11-23 11:57:41.956', '2023-11-23 11:58:30.614', '', '');
INSERT INTO `goods_category` VALUES (48, '33', 0, 22, 1, '2023-11-23 11:57:49.912', '2023-11-23 11:58:40.233', '', '');
INSERT INTO `goods_category` VALUES (49, '22', 0, 11, 1, '2023-11-23 11:57:57.907', '2023-11-23 11:58:23.798', '', '');
INSERT INTO `goods_category` VALUES (50, '33', 0, 22, 1, '2023-11-23 11:58:04.929', '2023-11-23 11:58:20.211', '', '');
INSERT INTO `goods_category` VALUES (51, '6', 0, 1, 1, '2023-11-23 11:58:44.748', '2023-11-23 11:58:51.081', '', '');
INSERT INTO `goods_category` VALUES (52, '32', 0, 24, 1, '2023-11-23 11:58:48.719', '2023-11-23 12:02:01.826', '', '');
INSERT INTO `goods_category` VALUES (53, '1', 1, 12, 1, '2023-11-23 21:39:03.934', '2023-11-25 10:12:51.040', '', '');
INSERT INTO `goods_category` VALUES (54, '3', 0, 3, 1, '2023-11-23 21:39:11.736', '2023-11-23 21:39:14.215', '', '');
INSERT INTO `goods_category` VALUES (55, '1217', 0, 15, 1, '2023-11-29 23:08:59.037', '2023-12-17 07:33:47.374', '', '');

-- ----------------------------
-- Table structure for goods_image
-- ----------------------------
DROP TABLE IF EXISTS `goods_image`;
CREATE TABLE `goods_image`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `goods_id` bigint(20) NOT NULL COMMENT '商品id',
  `image_url` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '图片url',
  `image_type` int(11) NOT NULL COMMENT '类型，1：商品图、2：介绍图',
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_image
-- ----------------------------
INSERT INTO `goods_image` VALUES (1, 18, '/resources/goods_6.jpg', 1, 0, '2023-10-30 23:31:59.469', '2023-10-30 23:31:59.469', '', '');
INSERT INTO `goods_image` VALUES (2, 18, '/resources/goods_6.jpg', 1, 0, '2023-10-30 23:32:06.900', '2023-10-30 23:32:06.900', '', '');
INSERT INTO `goods_image` VALUES (3, 18, '/resources/goods_6.jpg', 1, 0, '2023-10-30 23:32:14.672', '2023-10-30 23:32:14.672', '', '');

-- ----------------------------
-- Table structure for goods_item
-- ----------------------------
DROP TABLE IF EXISTS `goods_item`;
CREATE TABLE `goods_item`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '商品名称',
  `item_price` decimal(10, 2) NOT NULL COMMENT '售卖金额',
  `main_image` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主图',
  `item_desc` varchar(10000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '描述',
  `item_stock` int(11) NOT NULL DEFAULT 0 COMMENT '库存量',
  `category_id` bigint(20) NULL DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '状态 1：有效 0：无效',
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_item
-- ----------------------------
INSERT INTO `goods_item` VALUES (2, '枇杷', 50.00, '/resources/goods_5.jpg', '枇杷', 100, 1, 1, 0, '2023-10-03 20:38:14.562', '2023-12-07 00:08:22.493', '', '');
INSERT INTO `goods_item` VALUES (3, '杨梅', 60.00, '/resources/goods_6.jpg', '杨梅', 100, 1, 1, 0, '2023-10-03 20:38:53.375', '2023-12-07 00:08:23.109', '', '');
INSERT INTO `goods_item` VALUES (5, '枇杷2', 50.00, '/resources/goods_5.jpg', '枇杷', 100, NULL, 1, 0, '2023-10-03 20:38:14.562', '2023-10-29 09:27:49.438', '', '');
INSERT INTO `goods_item` VALUES (6, '杨梅2', 60.00, '/resources/goods_6.jpg', '杨梅', 100, NULL, 1, 0, '2023-10-03 20:38:53.375', '2023-10-29 10:12:26.456', '', '');
INSERT INTO `goods_item` VALUES (8, '枇杷3', 50.00, '/resources/goods_5.jpg', '枇杷', 100, NULL, 1, 0, '2023-10-03 20:38:14.562', '2023-10-29 09:27:51.555', '', '');
INSERT INTO `goods_item` VALUES (9, '杨梅3', 60.00, '/resources/goods_6.jpg', '杨梅', 100, NULL, 1, 0, '2023-10-03 20:38:53.375', '2023-10-29 09:27:52.328', '', '');
INSERT INTO `goods_item` VALUES (11, '枇杷4', 50.00, '/resources/goods_5.jpg', '枇杷', 99, NULL, 1, 0, '2023-10-03 20:38:14.562', '2024-01-20 19:45:09.089', '', '');
INSERT INTO `goods_item` VALUES (12, '杨梅4', 60.00, '/resources/goods_6.jpg', '杨梅', 100, NULL, 1, 0, '2023-10-03 20:38:53.375', '2023-10-29 09:27:54.581', '', '');
INSERT INTO `goods_item` VALUES (14, '枇杷5', 50.00, '/resources/goods_5.jpg', '枇杷', 99, NULL, 1, 0, '2023-10-03 20:38:14.562', '2024-02-07 17:30:35.346', '', '');
INSERT INTO `goods_item` VALUES (15, '杨梅5', 60.00, '/resources/goods_6.jpg', '杨梅', 91, NULL, 1, 0, '2023-10-03 20:38:53.375', '2024-02-07 17:29:58.526', '', '');
INSERT INTO `goods_item` VALUES (17, '枇杷6', 50.00, '/resources/goods_5.jpg', '枇杷', 0, NULL, 0, 0, '2023-10-03 20:38:14.562', '2023-12-06 00:48:57.458', '', '');

-- ----------------------------
-- Table structure for index_banner
-- ----------------------------
DROP TABLE IF EXISTS `index_banner`;
CREATE TABLE `index_banner`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(2550) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of index_banner
-- ----------------------------
INSERT INTO `index_banner` VALUES (1, '/resources/goods_6.jpg', 0, '2023-10-01 10:50:43.051', '2023-10-01 10:50:43.051', '', '');
INSERT INTO `index_banner` VALUES (2, '/resources/goods_5.jpg', 0, '2023-10-01 10:50:50.139', '2023-10-01 10:50:50.139', '', '');

-- ----------------------------
-- Table structure for order_info
-- ----------------------------
DROP TABLE IF EXISTS `order_info`;
CREATE TABLE `order_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL COMMENT 'userId',
  `item_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '商品名称',
  `item_price` decimal(10, 2) NOT NULL COMMENT '售卖金额',
  `item_image` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主图',
  `item_count` int(11) NOT NULL DEFAULT 0 COMMENT '数量',
  `remark` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '备注',
  `address_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `address_mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '收货人手机号码',
  `address_detail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '收货地址',
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '状态 ',
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 82 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_info
-- ----------------------------
INSERT INTO `order_info` VALUES (80, 1, '杨梅5', 60.00, '/resources/goods_6.jpg', 3, '', '222222', '1111111', '河北省石家庄市市辖区222', 3, 0, '2024-02-07 17:29:58.530', '2024-02-07 17:32:25.365', '', '');
INSERT INTO `order_info` VALUES (81, 1, '枇杷5', 50.00, '/resources/goods_5.jpg', 1, '', '张三1', '13800138000', '浙江省杭州市余杭区塘栖镇华联超市', 0, 0, '2024-02-07 17:30:35.348', '2024-02-07 17:30:35.348', '', '');

-- ----------------------------
-- Table structure for user_address
-- ----------------------------
DROP TABLE IF EXISTS `user_address`;
CREATE TABLE `user_address`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `mobile` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '收货人手机号码',
  `province_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '省名称',
  `city_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '市名称',
  `county_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '区域名称',
  `street_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '街道名称',
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '详细地址',
  `is_default` tinyint(1) NOT NULL DEFAULT 0 COMMENT '默认地址',
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '收货地址' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_address
-- ----------------------------
INSERT INTO `user_address` VALUES (20, 1, '张三2', '13800138000', '广东省', '深圳市', '南山区', '', '科技园2', 0, 0, '2024-01-24 23:00:38.545', '2024-01-24 23:21:23.439', '', '');
INSERT INTO `user_address` VALUES (21, 1, '张三3', '13800138000', '广东省', '深圳市', '南山区', '', '科技园3', 0, 1, '2024-01-24 23:01:15.441', '2024-01-24 23:28:26.946', '', '');
INSERT INTO `user_address` VALUES (22, 1, '222', '222', '河北省', '邯郸市', '市辖区', '', '222', 0, 1, '2024-01-24 23:23:04.216', '2024-01-24 23:28:23.841', '', '');
INSERT INTO `user_address` VALUES (23, 1, '222222', '1111111', '河北省', '石家庄市', '市辖区', '', '222', 0, 0, '2024-01-24 23:29:29.259', '2024-01-27 15:58:50.532', '', '');

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `openid` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'openid',
  `session_key` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'session_key',
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像',
  `nickname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '昵称',
  `is_deleted` tinyint(3) NOT NULL DEFAULT 0 COMMENT '是否删除，(0：正常，1：已删除)',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建时间',
  `update_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3) COMMENT '更新时间',
  `creator` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '创建人',
  `updater` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '更新人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
