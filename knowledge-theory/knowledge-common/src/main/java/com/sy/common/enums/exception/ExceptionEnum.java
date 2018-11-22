package com.sy.common.enums.exception;

/**
 * create by XiangChao on 2018/10/11
 */
public enum ExceptionEnum {
    /**
     * 文件未找到异常
     */
    FILE_NOT_FOUND("001", "文件未找到"),

    /**
     * 用户已存在
     */
    USER_ALREADY_EXISTS("002", "用户已存在"),

    /**
     * 用户不存在
     */
    USER_NOT_FOUND("003", "用户不存在"),

    /**
     * 老密码错误
     */
    OLD_PASSWORD_ERROR("004", "老密码错误"),

    /**
     * 验证码错误
     */
    VERIFICATION_CODE_ERROR("005", "验证码错误"),

    /**
     * 手机号已存在
     */
    PHONE_ALREADY_EXISTS("006", "手机号已存在"),

    /**
     * 文件类型不符合要求
     */
    File_Type_Error("007","文件类型不符合要求"),

    Params_Empty("008","参数为空"),






    Other_Exception("100","其他异常");



    private String code;
    private String message;

    ExceptionEnum(String code, String message) {
        this.code = code;
        this.message = message;
    }

    public String getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }
}
