package com.sy.dictionary.entity.domain;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
import java.sql.Timestamp;

/**
 * Created with IDEA
 * author:lhang
 * Date:2018/11/21
 * Time:18:10
 */
@Data
@Entity
@Table(name = "import_dic_record")
public class ImportDicRecord {
    @Id
    @GeneratedValue
    private Integer id;
    private String fileName;
    private String filePath;
    private String domainName;
    private String subDomainName;
    private String languagePair;
    private String createUser;
    private Integer dicCount;
    private Boolean deleted;
    private Timestamp gmtCreate;
    private Timestamp gmtUpdate;
}
