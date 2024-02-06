<template>
  <el-table-column type="expand" width="60">
    <template slot="header">
        <span>详情</span>
    </template>
    <template slot-scope="props">
      <el-form label-position="left" inline class="expand">
        <el-form-item label="排名：" >
          <span class="c1">{{ props.row.rank[0] }}/{{ props.row.rank[1] }}</span>
        </el-form-item>
        <el-form-item label="平均分：" >
          <span class="c2">{{ props.row.avg }}</span>
        </el-form-item>          
        <el-form-item label="已修人数：">
          <span class="c3">{{ props.row.selectedStudent }}/{{ props.row.totalStudent }}</span>
        </el-form-item>
        <el-form-item label="不及格人数:">
          <span class="c4">{{ props.row.notPassStudent }}</span>
        </el-form-item>          
      </el-form>
    </template>
  </el-table-column>
</template>

<script>
export default {
  name: "TableStuExpand",

}
</script>

<style lang="scss">
  .expand label {
    width: 150px;
    color: #88a0c5;
    margin-left: 10px;
  }
  .expand .el-form-item {
    margin-right: 400px;
    margin-bottom:c
  }

  .c1{
    margin-left: -100px;
    color: #c40404;
  }

  .c2{
    margin-left: -90px;
    color: #c40404;
  }

  .c3{
    margin-left: -80px;
    color: #c40404;
  }

  .c4{
    margin-left: -65px;
    color: #c40404;
  }
</style>