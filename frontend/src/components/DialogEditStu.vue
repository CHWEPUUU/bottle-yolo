<template>
    <el-dialog title="学生信息" :visible.sync="dialogFormVisible" width="30%" center>
        <el-form :model="form">
            <el-form-item label="学号" :label-width="formLabelWidth">
            <el-input disabled v-model="form.sno" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="姓名" :label-width="formLabelWidth">
            <el-input v-model="form.sname" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="性别" :label-width="formLabelWidth">
            <el-input disabled v-model="form.ssex" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="年龄" :label-width="formLabelWidth">
            <el-input v-model="form.sage" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="院系" :label-width="formLabelWidth">
            <el-input v-model="form.sdept" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button type="primary" @click="dialogFormVisible = false;Update()">确 定</el-button>
            <el-button @click="dialogFormVisible = false">取 消</el-button>
        </div>
    </el-dialog>
</template>

<script>
export default {
    name:"DialogEditStu",
    data() {
        return {
            dialogFormVisible: false,
            formLabelWidth: '100px',
            //学生信息表单
            form: {
                sno: '',
                sname: '',
                ssex: '',
                sage: 0,
                sdept: '',
            },
        }
    },
    methods: {
        Update(){
            //post传对象
            this.$axios.post('/update_student',this.form)     
        },
    },
    mounted() {
        this.$bus.$on('formStudent',(data)=>{
            this.dialogFormVisible = true,
            this.form = data
        })
    },
}
</script>

<style>

</style>