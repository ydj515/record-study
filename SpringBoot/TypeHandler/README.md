# SpringBoot - TypeHandler

- BooleanTypeHandler
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