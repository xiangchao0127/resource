package com.sy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * @author XiangChao
 * @date 2018/11/21
 */
public class XcTest {
    public static void main(String[] args) throws Exception{
        String command0 = "cd ../..&cd ..&cd svnWorkstation\\companyproject\\scrapy\\english_crawl\\debug";
        try {
            Process pro = Runtime.getRuntime().exec("cmd -k start python d:\\svnWorkstation\\companyproject\\scrapy\\english_crawl\\debug\\juku_debug.py"); //添加要进行的命令，"cmd/c calc"中calc代表要执行打开计算器，如何设置关机请自己查找cmd命令
            BufferedReader br = new BufferedReader(new InputStreamReader(pro
                    .getInputStream())); //虽然cmd命令可以直接输出，但是通过IO流技术可以保证对数据进行一个缓冲。
            String msg = null;
            while ((msg = br.readLine()) != null) {
                System.out.println(msg);
            }
            pro.waitFor();
        } catch (IOException exception) {
        }
    }
}
