//package com.sy.common.util;
//
//import com.language.knowledge.entity.dto.UserDetailDO;
//import org.springframework.security.core.context.SecurityContextHolder;
//
///**
// * @author XiangChao
// * @date 2018/10/16
// */
//public class SecurityUtils {
//    /**
//     * 获取当前用户
//     *
//     * @return
//     */
//    public static UserDetailDO getCurrentUser() {
//        UserDetailDO userDetails = (UserDetailDO) SecurityContextHolder.getContext()
//                .getAuthentication()
//                .getPrincipal();
//        return userDetails;
//    }
//}
