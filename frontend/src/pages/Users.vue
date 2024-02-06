<template>
  <div>
    <el-table ref="multipleTable" :data="tableData" border style="width:55%" height="450">

      <el-table-column fixed prop="id" label="用户名" width="100"></el-table-column>
      <el-table-column prop="role" label="角色" width="100"></el-table-column>
      <el-table-column prop="active" label="已启用" width="100"> </el-table-column>

      <el-table-column align="left" width="250">
        <template slot="header" >
          <!-- 增加用户，清空数据 -->
          <el-button size="small" type="primary" @click="dialogFormVisible = true;checkedModels = [];user.id = '';user.passwd = ''">添加</el-button>
          <el-button size="small" type="success" @click="reload()">刷新</el-button>
        </template>
        <template slot-scope="scope" >
          <el-button size="small" type="warning" @click="Edit(scope.row)">编辑</el-button>
          <el-button size="small" type="info" @click="Active(scope.row)"  v-if="scope.row.active === '是'">停用</el-button>
          <el-button size="small" type="info" @click="Active(scope.row)"  v-if="scope.row.active === '否'">启用</el-button>
          <el-button size="small" type="danger" @click="Delete(scope.row)">删除</el-button>           
        </template>
      </el-table-column>
      
    </el-table>

    <!-- 增加/编辑用户弹窗 -->
    <el-dialog title="用户信息" :visible.sync="dialogFormVisible" width="25%" center>
        <el-form :model="user">
            <el-form-item label="用户名" :label-width="formLabelWidth">
                <el-input  v-model.trim="user.id" autocomplete="off" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth">
                <el-input v-model="user.passwd" autocomplete="off" style="width: 150px" show-password></el-input>
            </el-form-item>
            <el-form-item label="角色" :label-width="formLabelWidth">
                <el-input disabled v-model="user.role" autocomplete="off" style="width: 150px"></el-input>            
            </el-form-item>

            <el-form-item label="权限" :label-width="formLabelWidth">
                <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox>
                <el-checkbox-group v-model="checkedModels" @change="handleCheckedModelsChange"> 
                  <el-checkbox v-for="model in models" :label="model" :key="model">{{model}}</el-checkbox> 
                </el-checkbox-group>
            </el-form-item>

            <el-form-item label="停用" :label-width="formLabelWidth">
                <el-checkbox v-model="inactive"></el-checkbox>             
            </el-form-item>
        </el-form>
        
        <div slot="footer" class="dialog-footer">
            <!-- 多个事件用;隔开 -->
            <el-button type="primary" @click="dialogFormVisible = false; ok()">确 定</el-button>
            <el-button @click="dialogFormVisible = false">取 消</el-button>
        </div>
    </el-dialog>

  </div>
</template>

<script>
export default {
  name:'Users',
  data() {
      return {
        dialogFormVisible: false,
        inactive: false,
        tableData:[],
        models:[],
        isIndeterminate: true,
        checkAll: false,
        checkedModels: [],
        user:{
          id: '', 
          pre_id:'', // 用于比较和新id
          passwd: '',
          pre_passwd:'', // 用于比较和新passwd
          role: 'GENERAL',
          active:'是',
        },
        formLabelWidth: '100px',
      }
  },
  methods: {
    ok(){
      console.log(this.checkedModels)
      if(this.inactive === true){
        this.user.active = '否'
      }
      if(this.user.id === '' || this.user.passwd === ''){
        alert('用户名和密码不能为空！')
        this.dialogFormVisible = true
      }
      if(this.user.id !== '' && this.user.passwd !== ''){
        this.$axios.post('/addEditUser', {user:this.user, models_id:this.checkedModels})
          .then(response => {
              console.log(response.data)
              },error => {
              console.log(error.message)
          })          
      }
      
    },
    Edit(row){
      // 编辑用户，获取用户原来数据
      this.checkedModels = [] // 先清空已有模型再获取
      this.user.id = row.id // 可更改id
      this.user.pre_id = row.id // 原id
      this.user.passwd = row.passwd // 可更改passwd
      this.user.pre_passwd = row.passwd // 原passwd
      console.log(row)
      //获取用户模型数据
      this.$axios.post('/userModels', {username:row.id})
      .then(response => {
        for (let i = 0; i < response.data.length; i++) {   
          this.checkedModels.push(response.data[i].value);           
        }
        },error => {
          console.log(error.message)
        })   
      this.dialogFormVisible = true
    },
    reload(){
      window.location.reload()
    },
    handleCheckAllChange(val) {
      this.checkedModels = val ? this.models : [];
      this.isIndeterminate = false;
      console.log(this.checkedModels)
    },
    handleCheckedModelsChange(value) {
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.models.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.models.length;
        console.log(this.checkedModels)
    },
    Active(row){
      if(row.role === 'ADMIN'){
        alert('ADMIN不可停用！');
      }
      // 更改用户激活状态
      else{
        if(row.active === '是'){
          this.$axios.post('/updateActive', {id:row.id, active:'否'}
          ).then(response => {
              console.log(response.data)
          },error => {
              console.log(error.message)
          })  
        }
        if(row.active === '否'){
          this.$axios.post('/updateActive', {id:row.id, active:'是'}
          ).then(response => {
              console.log(response.data)
          }, error => {
              console.log(error.message)
          })  
        }        
      }
    },
    Delete(row){
      if(row.role === 'ADMIN'){
        alert('ADMIN不可删除！');
      }
      else if(confirm("请确定要删除该信息！")){
        this.$axios.post('/deleteUser', {id:row.id})
        .then(response => {
            console.log(response.data)
        },error => {
            console.log(error.message)
        })        
      }
    },
  },
	mounted(){
    this.$axios.get('/users').then(response => {
        this.tableData = response.data
        console.log(response.data)
    },error => {
        console.log(error.message)
    })
    this.$axios.get('/models').then(response => {
      for (let i = 0; i < response.data.length; i++) {   
          this.models.push(response.data[i].model);           
      }
        console.log(this.models)
      },error => {
        console.log(error.message)
      })
  },
}
</script>

<style>

</style>