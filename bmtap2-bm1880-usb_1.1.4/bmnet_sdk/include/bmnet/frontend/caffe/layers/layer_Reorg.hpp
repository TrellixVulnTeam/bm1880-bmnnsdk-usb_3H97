/*
 * Copyright (C) Bitmain Technologies Inc.
 * All Rights Reserved.
 */
#ifndef _CAFFE_LAYER_REORG_H_
#define _CAFFE_LAYER_REORG_H_

#include <bmnet/frontend/caffe/CaffeFrontendContext.hpp>
#include <bmnet/frontend/caffe/CaffeLayer.hpp>

namespace bmnet {

class ReorgLayer : public CaffeLayer {
 public:
  explicit ReorgLayer(FrontendContext *ctx) : CaffeLayer(ctx) {}
  ~ReorgLayer() override = default;

  std::string layer_name() override { return std::string("Reorg"); }

  void dump() override {}
  void setup(TensorOp *op) override;
  void codegen(TensorOp *op) override;

 private:
};

}  // namespace bmnet
#endif
