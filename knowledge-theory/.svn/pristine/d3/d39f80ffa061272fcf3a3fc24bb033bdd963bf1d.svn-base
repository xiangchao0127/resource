package com.sy.common.util;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * 短信工具类
 *
 * @author XiangChao
 * @date 2018/10/18
 */
public class SmsUtils {

    private final static char[] HEX_DIGITS = {'0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    public static String sendSms(String accName, String accPwd, String mobies, String content) {
        StringBuffer sb = new StringBuffer("http://sdk.lx198.com/sdk/send?");
        try {
            sb.append("&accName=" + accName);
            sb.append("&accPwd=" + getMd5String(accPwd));
            sb.append("&aimcodes=" + mobies);
            sb.append("&content=" + URLEncoder.encode(content, "UTF-8"));
            sb.append("&dataType=string");
            URL url = new URL(sb.toString());
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
            return in.readLine();
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return null;
    }

    private static String bytes2hex(byte[] bytes) {
        StringBuffer sb = new StringBuffer();
        int t;
        for (int i = 0; i < 16; i++) {
            t = bytes[i];
            if (t < 0) {
                t += 256;
            }
            sb.append(HEX_DIGITS[(t >>> 4)]);
            sb.append(HEX_DIGITS[(t % 16)]);
        }

        return sb.toString();

    }


    public static String getMd5String(String strSrc) {
        MessageDigest md5 = null;
        try {
            md5 = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        return bytes2hex(md5.digest(strSrc.getBytes()));
    }

    /**
     * 随机生成6位随机验证码
     * 方法说明
     *
     * @return String
     * @Discription:扩展说明
     */
    public static String createRandomVcode() {
        //验证码
        String vcode = "";
        for (int i = 0; i < 6; i++) {
            vcode = vcode + (int) (Math.random() * 9);
        }
        return vcode;
    }

    public static void main(String[] args) {
        String randomVcode = createRandomVcode();
        System.out.println(sendSms("18244259758", "xiangchao111", "18244259758", "短信验证码:" + randomVcode + "【四川语言桥】"));
        System.out.println(randomVcode);
    }

}
