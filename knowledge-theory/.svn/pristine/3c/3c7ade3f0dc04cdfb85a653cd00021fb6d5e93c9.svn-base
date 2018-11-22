package com.sy.common.entity.dto;

import com.sy.common.enums.exception.ExceptionEnum;
import lombok.Data;

/**
 * @author XiangChao
 * @date 2018/10/12
 */
@Data
public class CustomException extends RuntimeException {
    /**
     * 编码
     */
    private String code;

    /**
     * 信息
     */
    private String msg;

    public CustomException(ExceptionEnum exceptionEnum, String explain) {
        this.code = exceptionEnum.getCode();
        this.msg = exceptionEnum.getMessage() + ":" + explain;
    }
}
