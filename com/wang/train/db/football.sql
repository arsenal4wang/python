-- ----------------------------
-- Table structure for `football`
-- ----------------------------
DROP TABLE IF EXISTS `football`;
CREATE TABLE `football` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `team` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `rank` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `round` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `win_num` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `ping_num` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `lose_num` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `cur_score` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `c_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=375 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of football
-- ----------------------------
