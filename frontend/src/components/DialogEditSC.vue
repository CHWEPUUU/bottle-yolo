<template>
  <!-- 增加课程弹窗 -->
  <el-dialog title="课程信息" :visible.sync="dialogFormVisible" width="30%" center>
    <el-form :model="form">
      <el-form-item label="课程号" :label-width="formLabelWidth">
        <el-input disabled v-model="form.cname" autocomplete="off" style="width: 150px"></el-input>
      </el-form-item>
      <el-form-item label="成绩" :label-width="formLabelWidth">
        <el-input v-model="form.grade" autocomplete="off" style="width: 150px"></el-input>
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
    name: "CourseInfo",
    data() {
    return {
      dialogFormVisible: false,
      form: {
        cname: '',
        grade: '',
        ccredit: ''
      },
      sc:{
        sno: '',
        cno: '',
        grade: '',
        status:null
      },
      course:{
        cno: '',
        cname: '',
        cpno: null,
        ccredit: ''
      },
      formLabelWidth: '120px',
      update: false,
    }
  },
  methods: {
    Update(){
        this.sc.grade = this.form.grade
        this.course.ccredit = this.form.ccredit

        // grade和ccredit分别属于两张不同的表,需要异步操作
        let updateData = async () => {
            try {
                //更新grade
                await this.$axios.post('/update_SC',this.sc);
                //更新ccredit
                await this.$axios.post('/update_course',this.course);
            } catch (error) {              
                console.error(error);
            }
        }
        // 调用updateData函数
        updateData();
    }
  },
    mounted() {
        this.$bus.$on('formSC',(data)=>{
            this.dialogFormVisible = true,
            this.form = data

            this.sc.cno = data.cno
            this.course.cno = data.cno
            this.course.cname = data.cname
        })
        this.$bus.$on('form_sno',(data)=>{
            this.sc.sno = data
        })
    }, 
}
</script>

<style>

</style>