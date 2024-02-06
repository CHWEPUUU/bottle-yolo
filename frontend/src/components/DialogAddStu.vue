<template>
     <!-- 增加学生弹窗 -->
    <el-dialog title="学生信息" :visible.sync="dialogFormVisible1" width="30%" center>
        <el-form :model="formStudent">
            <el-form-item label="学号" :label-width="formLabelWidth">
                <el-input  v-model="formStudent.sno" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="姓名" :label-width="formLabelWidth">
                <el-input v-model="formStudent.sname" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="性别" :label-width="formLabelWidth">
                <el-input  v-model="formStudent.ssex" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="年龄" :label-width="formLabelWidth">
                <el-input v-model="formStudent.sage" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="院系" :label-width="formLabelWidth">
                <el-input v-model="formStudent.sdept" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <!-- 多个事件用;隔开 -->
            <el-button type="primary" @click="dialogFormVisible1 = false;addStudent()">确 定</el-button>
            <el-button @click="dialogFormVisible1 = false">取 消</el-button>
        </div>
    </el-dialog>
</template>

<script>
export default {
    name: "DialogAddStu",
    //刷新页面
    inject: ['reload'],   
    data() {
        return {
            dialogFormVisible1: false,
            formStudent: {
                sno: '',
                sname: '',
                ssex: '',
                sage: 0,
                sdept: '',
            },
            formLabelWidth: '100px',
        }
    },
    methods: {
        addStudent(){
            //post传对象
            this.$axios.post('/add_student',this.formStudent)
            //刷新
            this.reload()
        },
    },
    //检测是否弹窗 
    mounted() {
        this.$bus.$on('dialogFormVisible1',(data)=>{
            this.dialogFormVisible1 = data
		})
    }
}
</script>

<style>

</style>