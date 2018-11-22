package com.sy.common.util;

import com.sy.common.config.constants.FileTypeConst;
import com.sy.common.entity.dto.BaseResponse;
import com.sy.common.entity.dto.TermResponse;
import com.sy.common.enums.StatusCodeEnum;
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
 * 解析单语文件内容供抓取
 *
 * @author Q00596
 */
public class AnalysisMonolingualFile {

    public static BaseResponse analysisMonoFile(String filePath) {
        BaseResponse baseResponse = new BaseResponse();
        //参数为空
        if (StringUtils.isEmpty(filePath)) {
            baseResponse.setCode(ExceptionEnum.Params_Empty.getCode());
            baseResponse.setMsg(ExceptionEnum.Params_Empty.getMessage());
            return baseResponse;
        }
        //文件为找到
        File file = new File(filePath);
        if (!file.exists()) {
            baseResponse.setCode(ExceptionEnum.FILE_NOT_FOUND.getCode());
            baseResponse.setMsg(ExceptionEnum.FILE_NOT_FOUND.getMessage());
            return baseResponse;
        }
        try {
            //返回类型
            List<String> returnStrLst = new ArrayList<>();

            FileInputStream fileInputStream = new FileInputStream(file);
            String suffix = file.getName().substring(file.getName().lastIndexOf(".") + 1).toLowerCase();
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
                    int rowLastIndex = sheet.getLastRowNum();
                    for (int i = 0; i <= rowLastIndex; i++) {
                        Row row = sheet.getRow(i);
                        Cell cell = row.getCell(0);
                        String cellStr = cell.getStringCellValue();
                        returnStrLst.add(cellStr);
                        //处理成功 返回
                        baseResponse.setCode(StatusCodeEnum.SUCCESS_STATUS.getCode());
                        baseResponse.setMsg(StatusCodeEnum.SUCCESS_STATUS.getMsg());
                        baseResponse.setObj(returnStrLst);
                    }
                    break;
                case FileTypeConst.SDLTB:
                    break;

                case FileTypeConst.TXT:
                    InputStreamReader inputStreamReader = new InputStreamReader(new FileInputStream(file));
                    BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                    //按照行读取字符串
                    String str;
                    while ((str = bufferedReader.readLine()) != null) {
                        returnStrLst.add(str);
                        baseResponse.setCode(StatusCodeEnum.SUCCESS_STATUS.getCode());
                        baseResponse.setMsg(StatusCodeEnum.SUCCESS_STATUS.getMsg());
                        baseResponse.setObj(returnStrLst);
                    }
                    break;

                default:
                    baseResponse.setCode(ExceptionEnum.File_Type_Error.getCode());
                    baseResponse.setMsg(ExceptionEnum.File_Type_Error.getMessage());
                    break;
            }
        } catch (Exception ex) {
            baseResponse.setCode(ExceptionEnum.Other_Exception.getCode());
            baseResponse.setMsg(ExceptionEnum.Other_Exception.getMessage());
        } finally {

        }

        return baseResponse;
    }
}
