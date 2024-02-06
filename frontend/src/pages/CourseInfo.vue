<template>
  <div>
    <el-table ref="multipleTable" :data="tableData" border style="width:57%" height="550"
              @selection-change="Selection">
    <el-table-column type="selection" width="40" ></el-table-column>

    <el-table-column fixed prop="sdept" label="院系" width="150"></el-table-column>
    <el-table-column prop="sname" label="姓名" width="150"></el-table-column>
    <el-table-column prop="grade" label="成绩" width="100"></el-table-column>

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
  <DialogEditCS></DialogEditCS>
  </div>
  
</template>

<script>
import DialogEditCS from '../components/DialogEditCS.vue'
export default {
	name:'CourseInfo',
  inject: ['reload'],
	data() {
		return {
      //选课学生信息
			tableData:[],
      course: [{cno:this.$route.query.course.cno}],
      studentSelection: []	
		}
	},
  components:{
    DialogEditCS
  },
  methods: {
    //获取选中信息
    Selection(val) {
      this.studentSelection = val;
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
          studentList:this.studentSelection,
          courseList:this.course  
      })        
        //刷新页面
        this.reload()
      }       
    },
    Edit(row){
      this.$bus.$emit('formCS',row)
      this.$bus.$emit('form_cno',this.$route.query.course.cno)
    },
    Delete(row){
      if(confirm("请确定要删除该信息！")){
          //post传参数
      this.$axios.post('/delete_SC',{
          studentList:[{sno:row.sno}],
          courseList:this.course
      })        
        //刷新页面
        this.reload()
      }
    },
  },
  //获取数据
	mounted(){
    //get传参 将路由query传参的课程号
    this.$axios.get('/student/cs',{
		params:{
      cno:this.$route.query.course.cno
		}
	}).then(
        response => {
          this.tableData = response.data
        },
        error => {
          console.log(error.message)
        }
      )
  },
}
</script>

<style>

</style>