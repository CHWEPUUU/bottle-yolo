<template>
  <!-- 课程弹窗 -->
  <el-dialog title="课程信息" :visible.sync="dialogFormVisible" width="30%" center>
    <el-form :model="formCourse">
      <el-form-item label="课程号" :label-width="formLabelWidth">
        <el-input disabled v-model="form.cno" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="课程名" :label-width="formLabelWidth">
        <el-input v-model="form.cname" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="先选课程号" :label-width="formLabelWidth">
        <el-input v-model="form.cpno" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="学分" :label-width="formLabelWidth">
        <el-input v-model="form.ccredit" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <!-- 多个事件用;隔开 -->
      <el-button type="primary" @click="dialogFormVisible = false;Update()">确 定</el-button>
      <el-button @click="dialogFormVisible = false">取 消</el-button>
    </div>
  </el-dialog>  
</template>

<script>

export default {
    name: 'DialogEditCourse',
    data() {
    return {
      dialogFormVisible: false,
      form: {
          cno: '',
          cname: '',
          cpno: null,
          ccredit: ''
      },
      formLabelWidth: '120px'
    }
  },
  methods: {
    Update(){
        this.$axios.post('/update_course',this.form)     
        
    }
  },
    mounted() {
        this.$bus.$on('formCourse',(data)=>{
            this.dialogFormVisible = true,
            this.form = data
        })
    }, 
}
</script>

<style>

</style>