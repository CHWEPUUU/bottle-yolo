<template>
  <!-- 增加课程弹窗 -->
  <el-dialog title="课程信息" :visible.sync="dialogFormVisible2" width="30%" center>
    <el-form :model="formCourse">
      <el-form-item label="课程号" :label-width="formLabelWidth">
        <el-input v-model="formCourse.cno" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="课程名" :label-width="formLabelWidth">
        <el-input v-model="formCourse.cname" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="先选课程号" :label-width="formLabelWidth">
        <el-input v-model="formCourse.cpno" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="学分" :label-width="formLabelWidth">
        <el-input v-model="formCourse.ccredit" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <!-- 多个事件用;隔开 -->
      <el-button type="primary" @click="dialogFormVisible2 = false;addCourse()">确 定</el-button>
      <el-button @click="dialogFormVisible2 = false">取 消</el-button>
    </div>
  </el-dialog> 
</template>

<script>
export default {
  name: "DialogAddCou",
  //刷新页面
  inject: ['reload'],
  data() {
    return {
      dialogFormVisible2: false,
      formCourse: {
          cno: '',
          cname: '',
          cpno: null,
          ccredit: ''
      },
      formLabelWidth: '120px'
    }
  },
  methods: {
    addCourse(){
      //post传对象
      this.$axios.post('/add_course',this.formCourse)
      //刷新
      this.reload()  
    }
  },
  //检测是否弹窗 
  mounted() {
    this.$bus.$on('dialogFormVisible2', (data) => {
        this.dialogFormVisible2 = data
    })
  }

}
</script>

<style>

</style>