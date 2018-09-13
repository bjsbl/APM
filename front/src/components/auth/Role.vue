<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addOrg'>新增角色</el-button>
      </el-col>
    </el-row>
      <el-table :data="roleList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
    </el-col>
    <el-dialog title="新增角色" :visible.sync="addRoleFormStatus" :close-on-click-modal="false">
        <el-form :model="roleForm" :rules="roleFormRules" label-width="80px">
            <el-form-item label="角色名称:" prop="reportFrom">
                <el-input v-model.trim="roleForm.reportFrom" auto-complete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addRoleFormStatus = false">取消</el-button>
            <el-button type="primary" @click="addRoleForm" :loading="loading">提交</el-button>
        </div>
    </el-dialog>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        loading:false,
        listLoading:false,
        addRoleFormStatus:false,
        roleFormRules: {},
        roleForm:{},
        roleList:[]
      }
    },
    methods:{
      getOrgList(){
        this.roleList = [{name:'Test'}]
      },
      addOrg(){
        this.addRoleFormStatus=true
      },
      addRoleForm(){
        
      }
    },
    mounted(){
      this.getOrgList()
    }
  }
</script>