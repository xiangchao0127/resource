package com.sy.common.util;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

/**
 * @author XiangChao
 * @date 2018/10/15
 */
public class ConfUtils {

    private Properties p = null;
    private static volatile ConfUtils confUtils = null;

    private ConfUtils() {

    }

    public static ConfUtils getInstance() {
        if (confUtils == null) {
            synchronized (ConfUtils.class) {
                if (confUtils == null) {
                    confUtils = new ConfUtils();
                }
            }
        }
        return confUtils;
    }

    /**
     * @param str
     * @return
     */
    public String getConfig(String str) {
        if (p == null) {
            p = new Properties();
        }
        try {
            p.load(new BufferedInputStream(new FileInputStream(ConfUtils.class.getClassLoader().getResource("application.properties").getPath())));
            return p.getProperty(str).trim();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

}


