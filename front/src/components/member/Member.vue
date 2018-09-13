<template>

  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addMember'>新增员工</el-button>
      </el-col>
    </el-row>
      <el-table :data="memberList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="姓名" sortable></el-table-column>
        <el-table-column prop="role" label="角色" sortable></el-table-column>
        <el-table-column prop="status" label="状态" sortable>
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
          </template>
        </el-table-column>
        <el-table-column prop="email" label="邮箱地址" sortable></el-table-column>
        <el-table-column prop="lastLoginTime" label="最近一次登录时间" sortable></el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total">
            </el-pagination>
    </el-col>
    <el-dialog title="编辑" :visible.sync="addMemberFormStatus" :close-on-click-modal="false">
        <el-form :model="memberForm" :rules="memberFormRules" label-width="80px">
            <el-form-item label="用户名:" prop="username">
                <el-input v-model.trim="memberForm.username" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码:" prop="password">
                <el-input v-model.trim="memberForm.password" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="邮箱:" prop="email">
                <el-input v-model.trim="memberForm.email" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="角色">
              <el-select v-model="memberForm.role" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
              </el-select>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addMemberFormStatus = false">取消</el-button>
            <el-button type="primary" @click="addMemberForm" :loading="loading">提交</el-button>
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
        addMemberFormStatus:false,
        listLoading:false,
        memberFormRules: {
          username: [
              { required: true, message: '请输入用户名', trigger: 'blur' },
              { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'blur' }
          ],
          password: [
              { required: true, message: '请输入密码', trigger: 'blur' },
              { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'blur' }
          ]
        },
        memberForm:{},
        memberList:[]
      }
    },
    methods:{
      getMemberList(){
        this.memberList = [{}]
      },
      addMember(){
        this.addMemberFormStatus=true
      },
      addMemberForm(){
        this.addMemberFormStatus=false
        this.$notify({
          title: '成功',
          message: '这是一条成功的提示消息',
          type: 'success'
        });
      }
    },
    mounted(){
      this.getMemberList()
    }
  }
</script>