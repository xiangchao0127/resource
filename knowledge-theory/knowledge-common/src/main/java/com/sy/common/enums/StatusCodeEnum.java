package com.sy.common.enums;

/**
 * 执行状态返回值
 * @author Q00596
 */
public enum StatusCodeEnum {


    SUCCESS_STATUS("200","成功"),




    ;


    StatusCodeEnum(String code, String msg) {
        this.code = code;
        this.msg = msg;
    }

    private String code;
    private String msg;

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }



}
