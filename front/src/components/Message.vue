<template>
  <el-row>
    <el-col :span="24">
      <el-table :data="messageList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name"></el-table-column>
        <el-table-column prop="description"></el-table-column>
        <el-table-column prop="createTime"></el-table-column>
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
        listLoading:false,
        messageList:[]
      }
    },
    methods:{
      getMessageList(){
        let _this = this
        _this.ajax.get("/static/mock/projectmodule.json").then(function(res){
          _this.messageList = res.data.result.data
        })
      }
    },
    mounted(){
      this.getMessageList()
    }
  }
</script>