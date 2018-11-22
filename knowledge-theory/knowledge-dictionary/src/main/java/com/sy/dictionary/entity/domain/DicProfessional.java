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
 * Time:17:48
 */
@Data
@Entity
@Table(name = "dic_professional")
public class DicProfessional {
    @Id
    @GeneratedValue
    private Integer id;
    private String dicName;
    private String linkedAreaId;
    private String linkedAreaName;
    private String imageUrl;
    private Integer sortWeight;
    private Timestamp gmtCreate;
    private Timestamp gmtUpdate;
    private String createUser;
    private Boolean deleted;
}
