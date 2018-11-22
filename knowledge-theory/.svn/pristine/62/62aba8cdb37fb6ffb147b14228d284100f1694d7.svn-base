package com.sy.common.util;

import com.sy.common.config.constants.FileTypeConst;
import com.sy.common.entity.dto.BaseResponse;
import com.sy.common.enums.StatusCodeEnum;
import com.sy.common.enums.exception.ExceptionEnum;
import org.apache.commons.lang.StringUtils;
import org.apache.poi.hwpf.extractor.WordExtractor;
import org.apache.poi.ooxml.POIXMLDocument;
import org.apache.poi.ooxml.extractor.POIXMLTextExtractor;
import org.apache.poi.openxml4j.opc.OPCPackage;
import org.apache.poi.xwpf.extractor.XWPFWordExtractor;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

/**
 * @author Q00596
 * 提取word文件的正文内容（无格式）
 */
public class AnalysisWordFile {

    public static BaseResponse analysisWordContent(String filePath) {

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
            String returnStr = "";
            String suffix = file.getName().substring(file.getName().lastIndexOf(".") + 1).toLowerCase();
            if (suffix.equals(FileTypeConst.DOC)) {
                InputStream is = new FileInputStream(file);
                WordExtractor ex = new WordExtractor(is);
                returnStr = ex.getText();
                ex.close();
                baseResponse.setCode(StatusCodeEnum.SUCCESS_STATUS.getCode());
                baseResponse.setMsg(StatusCodeEnum.SUCCESS_STATUS.getMsg());
                baseResponse.setObj(returnStr);
            } else if (suffix.equals(FileTypeConst.DOCX)) {
                OPCPackage opcPackage = POIXMLDocument.openPackage(filePath);
                POIXMLTextExtractor extractor = new XWPFWordExtractor(opcPackage);
                returnStr = extractor.getText();
                extractor.close();
                baseResponse.setCode(StatusCodeEnum.SUCCESS_STATUS.getCode());
                baseResponse.setMsg(StatusCodeEnum.SUCCESS_STATUS.getMsg());
                baseResponse.setObj(returnStr);
            } else {
                baseResponse.setCode(ExceptionEnum.File_Type_Error.getCode());
                baseResponse.setMsg(ExceptionEnum.File_Type_Error.getMessage());
            }
        } catch (Exception ex) {
            baseResponse.setCode(ExceptionEnum.Other_Exception.getCode());
            baseResponse.setMsg(ExceptionEnum.Other_Exception.getMessage());
        }
        return baseResponse;
    }
}
