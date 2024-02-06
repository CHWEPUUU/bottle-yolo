<template>
    <div>
    <el-table :data="tableData.filter(data => !search || data.cname.toLowerCase().includes(search.toLowerCase()))" 
        border stripe style="width:80%" height="500" :default-sort = "{prop: 'date', order: 'descending'}">    
        <TableCourseExpand></TableCourseExpand> 

        <el-table-column sortable prop="cno" label="课程号" width="150"></el-table-column>
        <el-table-column prop="cname" label="课程名" width="150"></el-table-column>
        <el-table-column prop="cpno" label="先选课程号" width="150"></el-table-column>
        <el-table-column sortable prop="ccredit" label="学分" width="100"></el-table-column>

        <el-table-column align="right" width="250">
            <template slot="header" slot-scope="scope">
                <el-input v-model="search" size="mini" placeholder="输入课程名搜索" @focus="scope"/>
            </template>
            <template slot-scope="{row}">
                <el-button size="small" type="primary" @click="Click(row)">查看</el-button>
                <el-button size="small" type="info" @click="Edit(row)">编辑</el-button>
                <el-button size="small" type="danger" @click="Delete(row)">删除</el-button>
            </template>
        </el-table-column>      
    </el-table>
    <DialogEditCourse ></DialogEditCourse >
    </div>
</template>

<script>
import DialogEditCourse from './DialogEditCourse.vue'
import TableCourseExpand from './TableCourseExpand.vue'


export default {
    name: "TableCourse",
    inject: ['reload'],
    data() {
        return {
            tableData: [],
            search: ''
        }
    },
    methods: {
        Click(row) {
        //路由跳转 query传参
        this.$router.push({
            path:'/course_info',
            query:{
                course:row
            }}).catch(err => {
                console.log(err)
            })
        },
        Edit(row){
            this.$bus.$emit('formCourse',row)          
        },
        Delete(row) {
            if(confirm("请确保该课程没有学生选修！") && confirm("请确定要删除该信息！")){
                //post传参数
                this.$axios.get('/delete',{
                    params:{
                        PrimaryKey:row.cno
                    }})
                    //刷新页面
                    this.reload()
            }  
        }      
    },
    components: {
        TableCourseExpand,
        DialogEditCourse
    },
    mounted() {
      this.$axios.post('/basic_course_info').then(
        response => {
          this.tableData = response.data
        },
        error => {
          console.log(error.message)
        })
    }
}
</script>

<style>

</style>