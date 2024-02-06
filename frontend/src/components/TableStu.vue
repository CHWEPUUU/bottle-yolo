<template>
    <div>
    <el-table :data="tableData.filter(data => !search || data.sname.toLowerCase().includes(search.toLowerCase()))" 
        border stripe style="width:100%" height="600" :default-sort = "{prop: 'date', order: 'descending'}">    
        <TableStuExpand></TableStuExpand>    

        <el-table-column sortable prop="sno" label="学号" width="200"></el-table-column>
        <el-table-column prop="sname" label="姓名" width="200"></el-table-column>
        <el-table-column sortable prop="ssex" label="性别" width="100"></el-table-column>
        <el-table-column sortable prop="sage" label="年龄" width="100"></el-table-column>
        <el-table-column sortable prop="sdept" label="院系" width="200"></el-table-column>

        <el-table-column align="right" width="250">
            <template slot="header" slot-scope="scope">
                <el-input v-model="search" size="mini" placeholder="输入姓名搜索" @focus="scope"/>
            </template>
            <template slot-scope="{row}">
                <el-button size="small" type="primary" @click="Check(row)">查看</el-button>
                <el-button size="small" type="info" @click="Edit(row)">编辑</el-button>
                <el-button size="small" type="danger" @click="Delete(row)">删除</el-button>
            </template>
        </el-table-column>  

    </el-table>
    <DialogEditStu></DialogEditStu>
    </div>
</template>

<script>
import DialogEditStu from './DialogEditStu.vue'
import TableStuExpand from './TableStuExpand.vue';

export default {   
    name: "TableStu", 
    //刷新页面
    inject: ['reload'],
    data() {
        return {
            tableData: [],
            search: ''
        };
    },
    components: {
        DialogEditStu,TableStuExpand
    },
    methods: {
        //查看学生选课信息
        Check(row) {
            //路由跳转 query传参
            this.$router.push({
                path:'/student_info',
                // name:'student_info',
                query:{ student:row }
            }).catch(err => {
                console.log(err)
                })            
        },
        //编辑学生信息默认内容
        Edit(row){
            this.$bus.$emit('formStudent',row)          
        },
        //删除学生信息
        Delete(row){
            if(confirm("请确保该学生没有选课！") && confirm("请确定要删除该信息！")){
                //post传参数
            this.$axios.get('/delete',{
                params:{
                    PrimaryKey:row.sno
                }})
                //刷新页面
                this.reload()
            }      
        }
    },
    //获取学生信息
    mounted () {
        //从后端获取数据给tableData
        this.$axios.post('/basic_student_info').then(
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