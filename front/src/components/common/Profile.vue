<template>
  <el-row>
    <el-col :span="24">
      <el-form :model="userForm" status-icon :rules="rules2" ref="userForm" label-width="80px" class="demo-ruleForm">
      <el-form-item label="真实姓名" prop="pass">
        <el-input type="password" v-model="userForm.realname" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="pass">
        <el-input type="password" v-model="userForm.pass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="checkPass">
        <el-input type="password" v-model="userForm.checkPass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="age">
        <el-input v-model.number="userForm.email"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary">提交</el-button>
      </el-form-item>
    </el-form>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    data(){
      return{
        userForm:{

        }
      }
    }
  }
</script>