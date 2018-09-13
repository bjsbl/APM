<template>
  <el-row>
    <el-col :span="24">
      <el-table :data="logList" v-loading="listLoading">
        <el-table-column prop="user" label="操作人"></el-table-column>
        <el-table-column prop="createTime" label="操作时间"></el-table-column>
        <el-table-column prop="description" label="描述"></el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        logList:[],
        listLoading:false
      }
    },
    methods:{
      getProjectDynamic(){
        let _this = this
        _this.ajax.get("/static/mock/dynamic.json").then(function(res){
          _this.logList = res.data.result.data
        })
      }
    },
    mounted(){
      this.getProjectDynamic()
    }
  }
</script>