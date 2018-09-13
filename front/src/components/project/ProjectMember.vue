<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model.trim="filters.name" placeholder="名称"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getProjectMemberList">查询</el-button>
        </el-form-item>
       <el-form-item>
        <el-button type='primary' @click='addProjectMember'>新增人员</el-button>
      </el-form-item>
      </el-form>
      </el-col>
    </el-row>
      <el-table :data="projectMemberList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="姓名" sortable></el-table-column>
        <el-table-column prop="role" label="权限" sortable></el-table-column>
        <el-table-column prop="email" label="邮箱地址" sortable></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>

      <el-dialog title="添加人员" :visible.sync="addProjectMemberVisible" :close-on-click-modal="false" >
        <el-row>
            <el-col :span="18">
                <el-table :data="memberList" highlight-current-row v-loading="memberListLoading">
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column prop="name" label="名称" sortable></el-table-column>
                    <el-table-column prop="email" label="Email" sortable></el-table-column>
                </el-table>
            </el-col>
        </el-row>
        <el-col :span="24" class="toolbar">
            <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
        </el-col>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addProjectMemberVisible = false">取消</el-button>
            <el-button type="primary" @click="addProjectMemberForm">提交</el-button>
        </div>
      </el-dialog>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        listLoading:false,
        memberListLoading:false,
        addProjectMemberVisible:false,
        memberList:[],
        projectMemberList:[],
        filters:{
          name:''
        }
      }
    },
    methods:{
      getProjectMemberList(){
        let _this = this
        _this.ajax.get("/static/mock/projectmember.json").then(function(res){
          _this.projectMemberList = res.data.result.data
        })
      },
      getMemberList(){
        let _this = this
        _this.ajax.get("/static/mock/projectmember.json").then(function(res){
          _this.memberList = res.data.result.data
        })
      },
      addProjectMember(){
        this.addProjectMemberVisible=true
        this.getMemberList()
      },
      addProjectMemberForm(){
        this.addProjectMemberVisible=false
      }
    },
    mounted(){
      this.getProjectMemberList()
    }
  }
</script>