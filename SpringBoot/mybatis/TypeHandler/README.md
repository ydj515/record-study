# SpringBoot - TypeHandler

- application.yml
```yml
spring:
    mybatis:
        type-aliases-package: molitapi.apiserver.model.*
        mapper-locations: classpath:mapper/*/*.xml
        config-location: classpath:mybatis-config.xml
        type-handlers-package: molitapi.apiserver.handler.typehandler
```
### BooleanTypeHandler
```java
@MappedJdbcTypes(JdbcType.CHAR)
@MappedTypes(Boolean.class)
public class BooleanTypeHandler extends BaseTypeHandler<Boolean> {

    private static final String YES = UseYnEnum.Y.name();
    private static final String NO = UseYnEnum.N.name();

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i,
                                    Boolean parameter, JdbcType jdbcType) throws SQLException {
        boolean b = parameter;
        ps.setString(i, b ? YES : NO);
    }

    @Override
    public Boolean getNullableResult(ResultSet rs, String columnName)
            throws SQLException {
        return convertStringToBooelan(rs.getString(columnName));
    }

    @Override
    public Boolean getNullableResult(ResultSet rs, int columnIndex)
            throws SQLException {
        return convertStringToBooelan(rs.getString(columnIndex));
    }

    @Override
    public Boolean getNullableResult(CallableStatement cs, int columnIndex)
            throws SQLException {
        return convertStringToBooelan(cs.getString(columnIndex));
    }

    private Boolean convertStringToBooelan(String strValue) throws SQLException {
        if (YES.equalsIgnoreCase(strValue)) {
            return Boolean.TRUE;
        } else if (NO.equalsIgnoreCase(strValue)) {
            return Boolean.FALSE;
        } else {
            return null;
        }
    }

}
```

- Member
```java
public class Member {
	private Boolean isIndividualMember;
}
```

- mybatis
```xml
<resultMap id="MemberMap" type="Member">
	<result column="INDVDL_MEMBER_YN" property="isIndividualMember" typeHandler="kr.go.test.handler.BooleanTypeHandler" />
</resultMap>
```

### LocalDateTimeTypeHandler
```java
@MappedTypes(LocalDateTime.class)
public class LocalDateTimeTypeHandler extends BaseTypeHandler<LocalDateTime> {

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, LocalDateTime parameter, JdbcType jdbcType)
            throws SQLException {
        ps.setTimestamp(i, Timestamp.valueOf(parameter));
    }

    @Override
    public LocalDateTime getNullableResult(ResultSet rs, String columnName) throws SQLException {
        Timestamp timestamp = rs.getTimestamp(columnName);
        return getLocalDateTime(timestamp);
    }

    @Override
    public LocalDateTime getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        Timestamp timestamp = rs.getTimestamp(columnIndex);
        return getLocalDateTime(timestamp);
    }

    @Override
    public LocalDateTime getNullableResult(CallableStatement cs, int columnIndex) throws SQLException {
        Timestamp timestamp = cs.getTimestamp(columnIndex);
        return getLocalDateTime(timestamp);
    }

    private static LocalDateTime getLocalDateTime(Timestamp timestamp) {
        if (timestamp != null) {
            return timestamp.toLocalDateTime();
        }
        return null;
    }
}
```

### LocalDateTypeHandler
```java
@MappedTypes(LocalDate.class)
public class LocalDateTypeHandler extends BaseTypeHandler<LocalDate> {

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, LocalDate parameter, JdbcType jdbcType)
            throws SQLException {
        ps.setDate(i, Date.valueOf(parameter));
    }

    @Override
    public LocalDate getNullableResult(ResultSet rs, String columnName) throws SQLException {
        Date date = rs.getDate(columnName);
        return getLocalDate(date);
    }

    @Override
    public LocalDate getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        Date date = rs.getDate(columnIndex);
        return getLocalDate(date);
    }

    @Override
    public LocalDate getNullableResult(CallableStatement cs, int columnIndex) throws SQLException {
        Date date = cs.getDate(columnIndex);
        return getLocalDate(date);
    }

    private static LocalDate getLocalDate(Date date) {
        if (date != null) {
            return date.toLocalDate();
        }
        return null;
    }
}
```