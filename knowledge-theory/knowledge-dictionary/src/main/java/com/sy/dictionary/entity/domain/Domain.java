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
 * Time:18:03
 */
@Data
@Entity
@Table(name = "domain")
public class Domain {
    @Id
    @GeneratedValue
    private String id;
    private String specialtyName;
    private Integer specialtyId;
    private String fullSpecialtyName;
    private Integer pSpecialtyId;
    private Boolean state;
    private Timestamp gmtCreate;
    private Timestamp gmtUpdate;
}
