package com.sy.common.util;

import java.io.*;
import java.util.List;

/**
 * Created with IDEA
 * author:lhang
 * Date:2018/11/20
 * Time:17:37
 */
public class FileUtils {
    /**
     * 将字符串写入到文件
     * @param filepath 文件全路径
     * @param str 字符串
     * @throws Exception
     */
    public static void write(String filepath, String str) throws Exception {
        makeFile(filepath);
        FileWriter writerEnglish = new FileWriter(filepath);
        BufferedWriter bwEn = new BufferedWriter(writerEnglish);

        bwEn.write(str);
        bwEn.close();
        writerEnglish.close();
    }

    /**
     * 将文件流写入到指定文件
     * @param filepath 文件全路径
     * @param fin 输入流
     */
    public static void write(String filepath, FileInputStream fin){
        try {
            OutputStream out = getFileOutputStream(filepath);
            byte[] buffer = new byte[1024 * 8];

            int readlength = -1;
            while ((readlength = fin.read(buffer)) != -1) {
                out.write(buffer, 0, readlength);
            }
            fin.close();
            out.close();
        }catch (IOException e){
            e.printStackTrace();
        }

    }
    /**
     * 获取指定路径下的输出流
     * @param filepath 文件全路径
     * @return
     */
    public static FileOutputStream getFileOutputStream(String filepath){
        File file = makeFile(filepath);
        FileOutputStream fout = null;
        try{
            fout = new FileOutputStream(file);
        }catch (Exception e){
            e.printStackTrace();
        }
        return fout;
    }


    /**
     * 创建文件
     *
     * @param filepath
     */
    private static File makeFile(String filepath) {
        File file = new File(filepath);
        if(!file.exists()){
            String dir = filepath.substring(0,filepath.lastIndexOf(File.separator));
            File dirFile = new File(dir);
            dirFile.mkdirs();
        }
        file = new File(filepath);
        return file;
    }

}
