<template>
    <div>
        <el-table :data="tableData.filter(data => !search || data.model.toLowerCase().includes(search.toLowerCase()))" 
            border stripe style="width:100%" height="600" :default-sort = "{prop: 'date', order: 'descending'}">     
            <el-table-column sortable prop="model" label="模型" width="100"></el-table-column>
            <el-table-column sortable prop="mAP50" label="mAP50" width="100"></el-table-column>
            <el-table-column sortable prop="mAP95" label="mAP50:95" width="150"></el-table-column>
            <el-table-column sortable prop="Recall" label="Recall" width="100"></el-table-column>
            <el-table-column sortable prop="Params" label="Params" width="100"></el-table-column>
            <el-table-column sortable prop="FLOPs" label="FLOPs" width="100" ></el-table-column>
            
            <el-table-column align="center" width="200">
                <template slot="header" slot-scope="scope">
                    <el-input v-model="search" size="mini" placeholder="请输入模型搜索" @focus="scope"/>
                </template>
            </el-table-column>  

        </el-table>
    </div>
  
</template>

<script>
export default {
    name:'ModelInfo',
    data() {
        return {
            tableData: [],
            search: ''
        }
    },
    methods: {
        Delete(row){
            if(confirm("请确定要删除该信息！")){
                this.$axios.post('/deleteImage', {id:row}).then(response => {
                    console.log(response.data)
                    window.location.reload()
                }).error(error => {
                    console.log(error.message)
                    window.location.reload()
                })
            }
        }
    },
	mounted(){
        this.$axios.get('/models')
        .then(response => {
            this.tableData = response.data
            console.log(response.data)
        },error => {
            console.log(error.message)
        })
  },

}
</script>

<style>

</style>