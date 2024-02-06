<template>
  <el-table-column type="expand" width="60">
    <template slot="header">
        <span>详情</span>
    </template>
    <template slot-scope="props">
      <el-form label-position="left" inline class="expand">
        <el-form-item label="排名：" >
          <span class="s1">{{ props.row.rank[0] }}/{{ props.row.rank[1] }}</span>
        </el-form-item>
        <el-form-item label="平均绩点：" >
          <span class="s2">{{ props.row.gpa }}</span>
        </el-form-item>          
        <el-form-item label="已修课程数：">
          <span class="s3">{{ props.row.selectedCourse }}/{{ props.row.totalCourse }}</span>
        </el-form-item>
        <el-form-item label="不及格课程数:">
          <span class="s4">{{ props.row.notPassCourse }}</span>
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
    margin-bottom: 0%;
  }

  .s1{
    margin-left: -100px;
    color: #c40404;
  }

  .s2{
    margin-left: -70px;
    color: #c40404;
  }

  .s3{
    margin-left: -60px;
    color: #c40404;
  }

  .s4{
    margin-left: -50px;
    color: #c40404;
  }
</style>