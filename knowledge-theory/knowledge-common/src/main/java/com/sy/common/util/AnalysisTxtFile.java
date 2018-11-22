package com.sy.common.util;


import com.sy.common.entity.dto.BaseResponse;
import com.sy.common.enums.StatusCodeEnum;
import com.sy.common.enums.exception.ExceptionEnum;
import org.apache.commons.lang.StringUtils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;

/**
 * 获取TXT文件内容
 *
 * @author Q00596
 */
public class AnalysisTxtFile {
    /**
     * 提取txt文本内容
     *
     * @param filePath 文件路径
     * @return
     */
    public static BaseResponse analysisTextContent(String filePath) {
        BaseResponse baseResponse = new BaseResponse();
        if (StringUtils.isEmpty(filePath)) {
            baseResponse.setCode(ExceptionEnum.Params_Empty.getCode());
            baseResponse.setMsg(ExceptionEnum.Params_Empty.getMessage());
            return baseResponse;
        }
        File file = new File(filePath);
        if (!file.exists()) {
            baseResponse.setCode(ExceptionEnum.FILE_NOT_FOUND.getCode());
            baseResponse.setMsg(ExceptionEnum.FILE_NOT_FOUND.getMessage());
            return baseResponse;
        }
        try {
            InputStreamReader inputStreamReader = new InputStreamReader(new FileInputStream(file));
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            //txt 文本内容
            String line = "";
            while ((bufferedReader.readLine()) != null) {
                line += bufferedReader.readLine();
            }
            inputStreamReader.close();
            baseResponse.setCode(StatusCodeEnum.SUCCESS_STATUS.getCode());
            baseResponse.setMsg(StatusCodeEnum.SUCCESS_STATUS.getMsg());
            baseResponse.setObj(line);
        } catch (Exception excepton) {
            baseResponse.setCode(ExceptionEnum.Other_Exception.getCode());
            baseResponse.setMsg(excepton.getMessage());
        } finally {

        }
        return baseResponse;
    }
}
