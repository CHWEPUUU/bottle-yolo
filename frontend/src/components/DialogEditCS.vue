<template>
  <!-- 增加课程弹窗 -->
  <el-dialog title="课程信息" :visible.sync="dialogFormVisible" width="30%" center>
    <el-form :model="form">
      <el-form-item label="院系" :label-width="formLabelWidth">
        <el-input v-model="form.sdept" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="姓名" :label-width="formLabelWidth">
        <el-input disabled v-model="form.sname" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="成绩" :label-width="formLabelWidth">
        <el-input v-model="form.grade" autocomplete="off" style="width: 150px"></el-input>
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
    name: "CourseInfo",
    data() {
    return {
      dialogFormVisible: false,
      form: {
        sdept: '',
        sname: '',
        grade: ''      
      },
      sc:{
        sno: '',
        cno: '',
        grade: '',
        status:null
      },
      student:{
        sno: '',
        sname: '',
        sdept:''
      },
      formLabelWidth: '120px',
      update: false,
    }
  },
  methods: {
    Update(){
        this.sc.grade = this.form.grade
        this.student.sdept = this.form.sdept

        // grade和sdept分别属于两张不同的表,需要异步操作
        let updateData = async () => {
            try {
                //更新grade
                await this.$axios.post('/update_SC',this.sc);
                //更新sdept
                await this.$axios.post('/update_student',this.student);
            } catch (error) {              
                console.error(error);
            }
        }
        // 调用updateData函数
        updateData();
    }
  },
    mounted() {
        this.$bus.$on('formCS',(data)=>{
            this.dialogFormVisible = true,
            this.form = data

            this.sc.sno = data.sno
            this.student.sno = data.sno           
            this.student.sname = data.sname
        })
        this.$bus.$on('form_cno',(data)=>{
            this.sc.cno = data          
        })
    }, 
}
</script>

<style>

</style>