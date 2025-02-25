/*
 * Copyright (C) Bitmain Technologies Inc.
 * All Rights Reserved.
 */
#ifndef _ONNX_LAYER_MULTIINPUT_H_
#define _ONNX_LAYER_MULTIINPUT_H_

#include <bmnet/frontend/onnx/OnnxFrontendContext.hpp>
#include <bmnet/frontend/onnx/OnnxOperator.hpp>

namespace bmnet {

class MultiInputOp : public OnnxOperator {
 public:
  explicit MultiInputOp(FrontendContext *ctx) : OnnxOperator(ctx) {}
  MultiInputOp(FrontendContext *ctx, const ONNX_NAMESPACE::Node *pOnnxNode)
      : OnnxOperator(ctx, pOnnxNode) {}
  ~MultiInputOp() override = default;

  std::string layer_name() override { return std::string("MultiInput"); }

  void dump() override;
  void setup(TensorOp *op) override;
  void codegen(TensorOp *op) override;
  OnnxOperator *makeOp(const ONNX_NAMESPACE::Node *node) override;

  void buildMemOperands() override;
};

}  // namespace bmnet

#endif /* _ONNX_LAYER_MULTIINPUT_H_ */
