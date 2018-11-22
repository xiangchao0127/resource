package com.sy.common.util;

import com.sy.common.config.constants.FileTypeConst;
import com.sy.common.entity.dto.BaseResponse;
import com.sy.common.entity.dto.TermResponse;
import com.sy.common.enums.exception.ExceptionEnum;
import org.apache.commons.lang3.StringUtils;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * @author Q00596
 * 提取excel tbx txt 格式双语术语内容
 */
public class AnalysisBilingualFile {

    /**
     * @param filePath
     * @return
     */
    public static BaseResponse analysisContent(String filePath) {
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
            List<TermResponse> termResponseLst = new ArrayList<>();
            String fileName = file.getName();

            String suffix = fileName.substring(fileName.lastIndexOf(".") + 1).toLowerCase();
            FileInputStream fileInputStream = new FileInputStream(filePath);
            Workbook workbook = null;
            switch (suffix) {
                case FileTypeConst.XLS:
                case FileTypeConst.XLSX:
                    if (suffix.equals(FileTypeConst.XLS)) {
                        workbook = new HSSFWorkbook(fileInputStream);
                    } else {
                        workbook = new XSSFWorkbook(fileInputStream);
                    }
                    Sheet sheet = workbook.getSheetAt(0);
                    //获取表头
                    Row rowHeader = sheet.getRow(0);
                    int lastRowNum = sheet.getLastRowNum();
                    for (int i = 0; i < lastRowNum; i++) {
                        Row row = sheet.getRow(i + 1);
                        //原文
                        Cell cell01 = row.getCell(0);
                        //译文
                        Cell cell02 = row.getCell(1);
                        //释义
                        Cell cell03 = row.getCell(2);
                        String cell01Str = cell01.getStringCellValue();
                        String cell02Str = cell02.getStringCellValue();
                        String cell03Str = cell03.getStringCellValue();
                        if (StringUtils.isEmpty(cell01Str) || StringUtils.isEmpty(cell02Str)) {
                            continue;
                        }
                        TermResponse termResponse = new TermResponse();
                        termResponse.setSourceText(cell01Str);
                        termResponse.setTargetText(cell02Str);
                        termResponse.setDesc(cell03Str);
                        termResponseLst.add(termResponse);
                        baseResponse.setObj(termResponseLst);
                        fileInputStream.close();
                    }
                    break;
                case FileTypeConst.TBX:


                    break;
                case FileTypeConst.CSV:
                    //TODO 暂时不支持
                    break;
                case FileTypeConst.TXT:
                    InputStreamReader inputStreamReader = new InputStreamReader(new FileInputStream(file));
                    BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                    //按照行读取字符串
                    String str;
                    while ((str = bufferedReader.readLine()) != null) {
                        String[] splitArray = str.split("\\t");
                        TermResponse termResponse = new TermResponse();
                        if (splitArray.length == 3) {
                            termResponse.setSourceText(splitArray[0]);
                            termResponse.setTargetText(splitArray[1]);
                            termResponse.setDesc(splitArray[2]);
                        } else if (splitArray.length == 2) {
                            termResponse.setSourceText(splitArray[0]);
                            termResponse.setTargetText(splitArray[1]);
                        }
                        termResponseLst.add(termResponse);
                        fileInputStream.close();
                    }
                    termResponseLst.remove(0);
                    baseResponse.setObj(termResponseLst);
                    break;
                default:
                    break;
            }
        } catch (Exception exception) {
            baseResponse.setCode(ExceptionEnum.Other_Exception.getCode());
            baseResponse.setMsg(ExceptionEnum.Other_Exception.getMessage());
            return baseResponse;
        } finally {

        }
        return baseResponse;
    }
}
