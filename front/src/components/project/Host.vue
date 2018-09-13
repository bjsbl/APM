<template>
  <el-row>
  <el-col :span="24">
    <el-button type="primary" @click="hostAdd">新增环境</el-button>
  </el-col>
  <el-col :span="24">
     <el-table :data="hostList" highlight-current-row>
        <el-table-column prop="name" label="名称" sortable>
        </el-table-column>
        <el-table-column prop="host" label="HOST" sortable>
        </el-table-column>
        <el-table-column prop="description" label="描述">
        </el-table-column>
        <el-table-column prop="status" label="状态">
          <template slot-scope="scope">
            <el-button type="info" size="small">{{scope.row.status===false?'启用':'禁用'}}</el-button>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
  </el-col>
  
  
   <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form :model="addForm" ref="addForm" label-width="80px">
          <el-form-item label="名称" prop="name">
              <el-input v-model.trim="addForm.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="Host" prop='host'>
              <el-input v-model.trim="addForm.host" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="描述" prop='description'>
              <el-input type="textarea" :rows="5" v-model.trim="addForm.description"></el-input>
          </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
      <el-button @click="addFormVisible = false">取消</el-button>
      <el-button type="primary" @click="addSubmit" :loading="addLoading">提交</el-button>
    </div>
    </el-dialog>
  </el-row>
</template>

<script>
  export default {
    data(){
      return{
        addFormVisible:false,
        addForm: {name: '',host: '',description: ''},
        addLoading:false,
        hostList:[]
      }
    },
    methods:{
      getHostList(){
        let _this = this
        _this.ajax.get("/static/mock/host.json").then(function(res){
          _this.hostList = res.data.result.data
        })
      },
      hostAdd(){
        this.addFormVisible = true
      },
      addSubmit(){

      }
    },
    mounted(){
      this.getHostList()
    }
  }
</script>