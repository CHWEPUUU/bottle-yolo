<template>
  <div>
    <el-table ref="multipleTable" :data="tableData" border style="width:55%" height="450"
              @selection-change="Selection">
      <el-table-column type="selection" width="40" ></el-table-column>

      <el-table-column fixed prop="cname" label="课程号" width="150"></el-table-column>
      <el-table-column prop="grade" label="成绩" width="100"></el-table-column>
      <el-table-column prop="ccredit" label="学分" width="100"> </el-table-column>

      <el-table-column align="right" width="200">
        <template slot="header" >
            <el-button size="small" type="success" @click="clearSelection()">取消选择</el-button>
            <el-button size="small" type="danger" @click="deleteSelection()">删除选择</el-button>
        </template>
        <template slot-scope="scope">
          <el-button size="small" type="info" @click="Edit(scope.row)">编辑</el-button>
          <el-button size="small" type="danger" @click="Delete(scope.row)">删除</el-button>           
        </template>
      </el-table-column>  

    </el-table>
    <DialogEditSC></DialogEditSC>
  </div>
</template>

<script>
import DialogEditSC from '../components/DialogEditSC.vue';
export default {
	name:'StudentInfo',
  inject: ['reload'],
	data() {
		return {
      tableData:[],
      student: [{sno:this.$route.query.student.sno}],		
      courseSelection: []
		}
	},
  components: {
    DialogEditSC
  },
  methods: {
    //获取选中信息
    Selection(val) {
      this.courseSelection = val;
    },
    //取消选择
    clearSelection(){
      this.$refs.multipleTable.clearSelection();
    },
    //删除选中
    deleteSelection(){
      if(confirm("请确定要删除该信息！")){
          //post传参数
      this.$axios.post('/delete_SC',{
          studentList:this.student,
          courseList:this.courseSelection  
      })        
        //刷新页面
        this.reload()
      }       
    },
    Edit(row){
      this.$bus.$emit('formSC',row)
      this.$bus.$emit('form_sno',this.$route.query.student.sno)
    },
    Delete(row){
      if(confirm("请确定要删除该信息！")){
          //post传参数
      this.$axios.post('/delete_SC',{
          studentList:this.student,
          courseList:[{cno:row.cno}]
      })        
        //刷新页面
        this.reload()
      }
    },
  },
  //获取传回的学生选课信息
	mounted(){
    // get传参 将路由query传参的学生学号
    this.$axios.post('/student/sc',{  
        sno:this.$route.query.student.sno   
    }).then(response => {
        this.tableData = response.data
      },error => {
        console.log(error.message)
      })
  },
}
</script>

<style lang="scss" scoped>

</style>