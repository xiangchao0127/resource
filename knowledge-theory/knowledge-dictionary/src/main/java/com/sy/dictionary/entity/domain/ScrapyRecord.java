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
 * Date:2018/11/22
 * Time:9:06
 */
@Data
@Entity
@Table(name = "scrapy_record")
public class ScrapyRecord {
    @Id
    @GeneratedValue
    private Integer id;
    private String webUrl;
    private String webName;
    private String type;
    private Character scrapyField;
    private String createUser;
    private String scrapyState;
    private Integer uploadCount;
    private Integer scrapyCount;
    private String  uploadFileUrl;
    private String  downloadFileUrl;
    private Timestamp gmtCreate;
    private Timestamp gmtUpdate;
    private Timestamp scrapyStartTime;
    private Timestamp scrapyEndTime;
    private Boolean deleted;
}
