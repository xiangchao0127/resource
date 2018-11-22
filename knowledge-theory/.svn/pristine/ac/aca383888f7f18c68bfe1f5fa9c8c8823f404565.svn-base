package com.sy.common.util;


import java.sql.Timestamp;
import java.text.SimpleDateFormat;

/**
 * @author XiangChao
 * @date 2018/10/16
 */
public final class DateUtils extends org.apache.commons.lang3.time.DateUtils {
    static final SimpleDateFormat SIMPLE_DATEFORMAT = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    static final SimpleDateFormat SIMPLE_DATEFORMAT_ORDER = new SimpleDateFormat("yyyyMMddHHmm");

    /**
     * 获取当前时间
     *
     * @return
     */
    public static Timestamp getCurrentTimeStamp() {
        Timestamp timestamp = new Timestamp(System.currentTimeMillis());
        return timestamp;
    }

    /**
     * 获取明年当前时间
     *
     * @return
     */
    public static Timestamp getNextYeartCurrentTimeStamp() {
        Timestamp timestamp = null;
        synchronized (SIMPLE_DATEFORMAT) {
            timestamp = new Timestamp(System.currentTimeMillis() + 3600 * 24 * 365 * 1000L);
        }
        return timestamp;
    }

    public static String timeStamp2Str(Timestamp timestamp) {
        String format = null;
        synchronized (SIMPLE_DATEFORMAT) {
            format = SIMPLE_DATEFORMAT.format(timestamp);
        }
        return format;
    }

    public static String timeStamp2StrForOrderNum(Timestamp timestamp) {
        String format = null;
        synchronized (SIMPLE_DATEFORMAT_ORDER) {
            format = SIMPLE_DATEFORMAT_ORDER.format(timestamp);
        }
        String num = "";
        int i = 0;
        for (;i < 3;i++){
            num += (int)(Math.random() * 9) ;
        }
        return format + num;
    }
}
